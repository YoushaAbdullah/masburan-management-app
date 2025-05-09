"use client";

import { useEffect, useState } from "react";
import axios from "axios";
import { AppSidebar } from "@/components/app-sidebar";
import { ChartAreaInteractive } from "@/components/chart-area-interactive";
import { DataTable } from "@/components/data-table";
import { SectionCards } from "@/components/section-cards";
import { SiteHeader } from "@/components/site-header";
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar";
import { z } from "zod";
import data from "./data.json";
import {
  BoqType,
  ProjectType,
  InventoryType,
  CombinedDataType,
  combined_schema,
} from "@/lib/validation";

const DashboardPage: React.FC = () => {
  const [fetchedData, setFetchedData] = useState<CombinedDataType | null>(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const token = localStorage.getItem("accessToken"); // Retrieve the token from localStorage
      console.log("Access Token:", token); // Log the access token to the console

      const [boqRes, inventoryRes] = await Promise.all([
        axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/boq/create/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
        // axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/projects/create/`, {
        //   headers: { Authorization: `Bearer ${token}` },
        // }),
        axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/inventory/create/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
      ]);

      const parsed = combined_schema.parse({
        boq: boqRes.data,
        //project: projectRes.data,
        inventory: inventoryRes.data,
      });
      setFetchedData(parsed);
      console.log("Fetched and parsed data:", parsed);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "calc(var(--spacing) * 72)",
          "--header-height": "calc(var(--spacing) * 12)",
        } as React.CSSProperties
      }
    >
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
        <div className="flex flex-1 flex-col">
          <div className="@container/main flex flex-1 flex-col gap-2">
            <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
              <SectionCards />
              <div className="px-4 lg:px-6">
                <ChartAreaInteractive />
              </div>
              <DataTable data={data} />
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  );
};

export default DashboardPage;
