import { Table } from "antd";
import React from "react";

//Navigation menu
//Users view - When click one, detail expands.
//Tasks view - List all task - SEARCH BAR - FILTER BY COMPLETED OR USER_ID - PAGINATION

interface User {
  key: string;
  name: string;
  username: string;
  email: string;
  address: string;
  description: string;
}

// interface Task {
//   id: number;
//   user_id: number;
//   title: string;
//   completed: boolean;
// }

interface Column {
  title: string;
  dataIndex: string;
  key: string;
}

interface GenericTableProps {
  dataSource: User[] | undefined;
  columns: Column[];
}

export default function GenericTable({
  dataSource,
  columns,
}: GenericTableProps) {
  return (
    <Table
      dataSource={dataSource}
      columns={columns}
      tableLayout={"fixed"}
      expandable={{
        expandedRowRender: (row) => (
          <b style={{ margin: 0 }}>{row.description}</b>
        ),
        rowExpandable: (record) => record.name !== "Not Expandable",
      }}
    />
  );
}
