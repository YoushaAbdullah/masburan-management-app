import axios from "axios";
import { CombinedDataType, combined_schema } from "@/lib/validation";

export const fetchData = async (): Promise<CombinedDataType | null> => {
  try {
    const token = localStorage.getItem("accessToken"); // Retrieve the token from localStorage
    if (!token) {
      console.error("No access token found.");
      return null;
    }

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

    console.log("Fetched and parsed data:", parsed);
    return parsed;
  } catch (error) {
    console.error("Error fetching data:", error);
    return null;
  }
};
