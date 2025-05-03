"use client";

import { useEffect, useState } from "react";
import axios from "axios";
import { AppSidebar } from "@/components/app-sidebar";
import { ChartAreaInteractive } from "@/components/chart-area-interactive";
import { DataTable } from "@/components/data-table";
import { SectionCards } from "@/components/section-cards";
import { SiteHeader } from "@/components/site-header";
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar";

import data from "./data.json";

// Define interfaces for each data type
interface Project {
  id: number;
  name: string;
  code: string;
  description: string;
  startDate: string;
  endDate: string;
}

interface BOQ {
  id: number;
  project: number;
  material: string;
  quantity: number;
  unitPrice: number;
  totalCost: number;
}

interface DeliveryOrder {
  id: number;
  orderNumber: string;
  date: string;
  project: number;
  status: string;
}

interface DeliveryOrderDetails {
  id: number;
  deliveryOrder: number;
  item: string;
  quantity: number;
  unitPrice: number;
}

interface Invoice {
  id: number;
  number: string;
  amount: number;
  date: string;
  project: number;
  status: string;
}

interface InvoiceDetails {
  id: number;
  invoice: number;
  description: string;
  amount: number;
  tax: number;
}

interface FDPReport {
  id: number;
  reportName: string;
  date: string;
  project: number;
  status: string;
}

interface Inventory {
  id: number;
  item: string;
  quantity: number;
  location: string;
  status: string;
}

interface ExternalInventory {
  id: number;
  supplier: string;
  item: string;
  quantity: number;
  unitPrice: number;
}

interface ItemList {
  id: number;
  name: string;
  category: string;
  description: string;
  unitPrice: number;
}

// Define a type for the fetched data
// interface FetchedData {
//   project: Project[];
//   boq: BOQ[];
//   deliveryOrder: DeliveryOrder[];
//   deliveryOrderDetails: DeliveryOrderDetails[];
//   invoice: Invoice[];
//   invoiceDetails: InvoiceDetails[];
//   fdpReport: FDPReport[];
//   inventory: Inventory[];
//   externalInventory: ExternalInventory[];
//   itemList: ItemList[];
// }

const DashboardPage: React.FC = () => {
  const [notes, setFetchedData] = useState<BOQ[]>([]);
  const [material, setMaterial] = useState<string>("");
  const [quantity, setQuantity] = useState<number>(0);
  const [unitPrice, setUnitPrice] = useState<string>("");
  const [totalCost, setTotalCost] = useState<string>("");

  // const [fetchedData, setFetchedData] = useState<FetchedData>({
  //   project: [],
  //   boq: [],
  //   deliveryOrder: [],
  //   deliveryOrderDetails: [],
  //   invoice: [],
  //   invoiceDetails: [],
  //   fdpReport: [],
  //   inventory: [],
  //   externalInventory: [],
  //   itemList: [],
  // });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const token = localStorage.getItem("accessToken"); // Retrieve the token from localStorage
      console.log("Access Token:", token); // Log the access token to the console

      const response = await axios.get(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/boq/create/`,
        {
          headers: {
            Authorization: `Bearer ${token}`, // Include the token in the Authorization header
          },
        }
      );
      setFetchedData(response.data);
      console.log("Fetched Data:", response.data); // Log the fetched data to the console
    } catch (error) {
      console.error("Error fetching boq:", error);
      alert("Failed to fetch boq.");
    }
  };

  // const endpoints = [
  //   {
  //     key: "project",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/project/`,
  //   },
  //   { key: "boq", url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/boq/` },
  //   {
  //     key: "deliveryOrder",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/delivery-order/`,
  //   },
  //   {
  //     key: "deliveryOrderDetails",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/delivery-order-details/`,
  //   },
  //   {
  //     key: "invoice",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/invoice/`,
  //   },
  //   {
  //     key: "invoiceDetails",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/invoice-details/`,
  //   },
  //   {
  //     key: "fdpReport",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/fdp-report/`,
  //   },
  //   {
  //     key: "inventory",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/inventory/`,
  //   },
  //   {
  //     key: "externalInventory",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/external-inventory/`,
  //   },
  //   {
  //     key: "itemList",
  //     url: `${process.env.NEXT_PUBLIC_BACKEND_URL}/item-list/`,
  //   },
  // ];

  // const results = await Promise.all(
  //   endpoints.map(async (endpoint) => {
  //     const response = await axios.get(endpoint.url, {
  //       headers: {
  //         Authorization: `Bearer ${token}`, // Include the token in the Authorization header
  //       },
  //     });
  //     return { key: endpoint.key, data: response.data };
  //   })
  // );

  // const data = results.reduce(
  //   (acc, result) => {
  //     // Type narrowing ensures we only assign known keys
  //     if (result.key in acc) {
  //       acc[result.key as keyof FetchedData] = result.data;
  //     }
  //     return acc;
  //   },
  //   {
  //     project: [],
  //     boq: [],
  //     deliveryOrder: [],
  //     deliveryOrderDetails: [],
  //     invoice: [],
  //     invoiceDetails: [],
  //     fdpReport: [],
  //     inventory: [],
  //     externalInventory: [],
  //     itemList: [],
  //   } as FetchedData
  // );

  //     setFetchedData(data);
  //     console.log("Fetched Data:", data);
  //   } catch (err) {
  //     console.error("Error fetching data:", err);
  //     setError("Failed to fetch data. Please try again later.");
  //   }
  // };

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
