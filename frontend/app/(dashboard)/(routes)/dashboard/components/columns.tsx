"use client";

import { ColumnDef } from "@tanstack/react-table";

export type Payment = {
<<<<<<< HEAD
  id: number;
  date: string;
  amount: string;
=======
  order_id: string;
  date: string;
  amount: number;
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
  status: "Success" | "Pending" | "Rejected";
  transaction_type: "Bought" | "Sold";
};

export const columns: ColumnDef<Payment>[] = [
  {
<<<<<<< HEAD
    accessorKey: "id",
    header: "ID",
=======
    accessorKey: "order_id",
    header: "Order ID",
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
  },
  {
    accessorKey: "date",
    header: "Date",
  },
  {
    accessorKey: "amount",
    header: () => <div className="text-left">Amount</div>,
    cell: ({ row }) => {
      const amount = parseFloat(row.getValue("amount"));
      const formatted = new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
      }).format(amount);

      return <div className="text-left font-medium">{formatted}</div>;
    },
  },
  {
    accessorKey: "transaction_type",
    header: "Transaction Type",
  },
  {
    accessorKey: "status",
    header: "Status",
  },
];
