import { description } from "@/components/chart-area-interactive";
import { z } from "zod";

// BOQ schema
export const boq_schema = z.object({
  id: z.number(),
  job_description: z.string(),
  mm_no: z.number(),
  project: z.number(),
  quantity: z.number(),
  unit_rate: z.number(),
  uom: z.string(),
  boq_date: z.string().date(),
});
//
// Project schema
export const project_schema = z.object({
  id: z.number(),
  project_code: z.string(),
  project_name: z.string(),
  project_type: z.string(),
  project_start_date: z.string().date(),
  project_complete_date: z.string().date(),
});
//External Inventory schema
export const external_inventory_schema = z.object({
  id: z.number(),
  material_name: z.string(),
  specification: z.string(),
  unit: z.string(),
  quantity_ordered: z.number(),
  quantity_ordered_unit_price: z.number(),
  quantity_stock: z.number(),
  quantity_stock_unit_price: z.number(),
  quantity_stock_acquired_from_site_name: z.string(),
  supplier: z.string(),
  contact_no_supplier: z.string(),
  delivery_method: z.string(),
  delivery_details: z.string(),
  project: z.number(),
});
// Inventory schema
export const inventory_schema = z.object({
  id: z.number(),
  material_name: z.string(),
  specification: z.string(),
  unit: z.string(),
  quantity_ordered: z.number(),
  quantity_ordered_unit_price: z.number(),
  quantity_stock: z.number(),
  quantity_stock_unit_price: z.number(),
  quantity_stock_acquired_site_name: z.string(),
  supplier: z.string(),
  contact_no_supplier: z.string(),
  delivery_method: z.string(),
  delivery_details: z.string(),
  project: z.number(),
});
// Delivery order schema
export const delivery_order_schema = z.object({
  id: z.number(),
  item_code: z.string(),
  description: z.string(),
  uom: z.string(),
  unit_price: z.number(),
  quantity: z.number(),
  project: z.number(),
  delivery_order_details: z.number(),
});
// Delivery order details schema
export const delivery_order_details_schema = z.object({
  do_no: z.string(),
  po_no: z.string(),
  date: z.string().date(),
  project_location: z.string(),
  attn_to: z.string(),
  project_codename: z.string(),
  declaration: z.string(),
  delivery_location: z.string(),
  delivery_order_percentage: z.number(),
  delivery_company_name: z.string(),
});
//Invioce schema
export const invoice_schema = z.object({
  item_code: z.string(),
  description: z.string(),
  uom: z.string(),
  unit_price: z.number(),
  quantity: z.number(),
  invoice_details: z.number(),
  project: z.number(),
});
// Invoice details schema
export const invoice_details_schema = z.object({
  inv_no: z.string(),
  po_no: z.string(),
  date: z.string(),
  project_location: z.string(),
  attn_to: z.string(),
  project_codename: z.string(),
  payment_terms: z.string(),
  account: z.string(),
  invoice_to_company_location: z.string(),
  invoice_percentage: z.number(),
  invoice_company_name: z.string(),
  project: z.number(),
});
//Item list schema
export const item_list_schema = z.object({
  id: z.number(),
  material_name: z.string(),
  specification: z.string(),
  unit: z.string(),
  unit_price: z.number(),
  supplier: z.string(),
  contact_no_supplier: z.string(),
});
// Type inference
export type BoqType = z.infer<typeof boq_schema>;
export type ProjectType = z.infer<typeof project_schema>;
export type InventoryType = z.infer<typeof inventory_schema>;
export type ExternalInventoryType = z.infer<typeof external_inventory_schema>;
export type DeliveryOrderType = z.infer<typeof delivery_order_schema>;
export type DeliveryOrderDetailsType = z.infer<
  typeof delivery_order_details_schema
>;
export type InvoiceType = z.infer<typeof invoice_schema>;
export type InvoiceDetailsType = z.infer<typeof invoice_details_schema>;
export type ItemListType = z.infer<typeof item_list_schema>;

// Combined schema (optional)
export const combined_schema = z.object({
  boq: z.array(boq_schema),
  project: z.array(project_schema),
  inventory: z.array(inventory_schema),
  external_inventory: z.array(external_inventory_schema),
  delivery_order: z.array(delivery_order_schema),
  delivery_order_details: z.array(delivery_order_details_schema),
  invoice: z.array(invoice_schema),
  invoice_details: z.array(invoice_details_schema),
  item_list: z.array(item_list_schema),
});

export type CombinedDataType = z.infer<typeof combined_schema>;
