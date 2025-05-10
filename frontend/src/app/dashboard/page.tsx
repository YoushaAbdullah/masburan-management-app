"use client";

import React, { useEffect, useState } from "react";
import { DataTable } from "@/components/data-table";
import Layout from "@/app/dashboard/layout";
import axios from "axios";
import { AppSidebar } from "@/components/app-sidebar";
import { ChartAreaInteractive } from "@/components/chart-area-interactive";
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

      const [
        boqRes,
        projectRes,
        inventoryRes,
        externalinventoryRes,
        deliveryorderRes,
        deliveryorderdetailsRes,
        invoiceRes,
        invoicedetailsRes,
        itemlistRes,
      ] = await Promise.all([
        axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/boq/create/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
        axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/projects/create/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
        axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/inventory/create/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
        axios.get(
          `${process.env.NEXT_PUBLIC_BACKEND_URL}/external-inventory/create/`,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        ),
        axios.get(
          `${process.env.NEXT_PUBLIC_BACKEND_URL}/delivery-order/create/`,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        ),
        axios.get(
          `${process.env.NEXT_PUBLIC_BACKEND_URL}/delivery-order-details/create/`,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        ),
        axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/invoice/create/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
        axios.get(
          `${process.env.NEXT_PUBLIC_BACKEND_URL}/invoice-details/create/`,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        ),
        axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/item-list/create/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
      ]);

      const parsed = combined_schema.parse({
        boq: boqRes.data,
        project: projectRes.data,
        inventory: inventoryRes.data,
        external_inventory: externalinventoryRes.data,
        delivery_order: deliveryorderRes.data,
        delivery_order_details: deliveryorderdetailsRes.data,
        invoice: invoiceRes.data,
        invoice_details: invoicedetailsRes.data,
        item_list: itemlistRes.data,
      });
      setFetchedData(parsed);
      console.log("Fetched and parsed data:", parsed);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <>
      <SectionCards />
      <div className="px-4 lg:px-6">
        <ChartAreaInteractive />
      </div>
      <DataTable data={data} />
    </>
  );
};

export default DashboardPage;
