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
import { fetchData } from "@/lib/fetch-data";
import data from "./data.json";
import { CombinedDataType } from "@/lib/validation";

const DashboardPage: React.FC = () => {
  const [fetchedData, setFetchedData] = useState<CombinedDataType | null>(null);

  useEffect(() => {
    getData();
  }, []);

  const getData = async () => {
    const data = await fetchData();
    setFetchedData(data);
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
