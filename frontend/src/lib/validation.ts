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
  boq_date: z.string().date(), // or just z.string() if it's plain ISO string
});

// Project schema
export const project_schema = z.object({
  id: z.number(),
  project_code: z.string(),
  project_name: z.string(),
  project_start_date: z.string().date(),
  project_complete_date: z.string().date(),
});

// Inventory schema
export const inventory_schema = z.object({
  id: z.number(),
  material_name: z.string(),
  specification: z.string(),
  unit: z.string(),
  quantity_ordered: z.number(), // Ensure quantity_ordered is a string
  quantity_ordered_unit_price: z.number(), // Ensure quantity_ordered_unit_price is a string
  quantity_stock: z.number(), // Ensure quantity_stock is a string
  quantity_stock_unit_price: z.number(), // Ensure quantity_stock_unit_price is a string
  quantity_stock_acquired_site_name: z.string(),
  supplier: z.string(),
  contact_no_supplier: z.string(),
  delivery_method: z.string(),
  delivery_details: z.string(),
  project: z.number(),
});

// Type inference
export type BoqType = z.infer<typeof boq_schema>;
export type ProjectType = z.infer<typeof project_schema>;
export type InventoryType = z.infer<typeof inventory_schema>;

// Combined schema (optional)
export const combined_schema = z.object({
  boq: z.array(boq_schema),
  //project: z.array(project_schema),
  inventory: z.array(inventory_schema),
});

export type CombinedDataType = z.infer<typeof combined_schema>;
