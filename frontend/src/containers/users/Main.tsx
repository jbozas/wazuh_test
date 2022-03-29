import React from "react";
import useFetch from "../useFetch";
import GenericTable from "../../components/Table";

interface tableProps {
  visible: boolean;
}

export default function Main({ visible }: tableProps) {
  const columns = [
    {
      title: "ID",
      dataIndex: "id",
      key: "key",
    },
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Username",
      dataIndex: "username",
      key: "username",
    },
    {
      title: "Email",
      dataIndex: "email",
      key: "email",
    },
  ];

  const { data } = useFetch("users");

  return (
    <>
      {visible ? (
        <div>
          {data && visible && (
            <GenericTable dataSource={data} columns={columns} />
          )}
        </div>
      ) : null}
    </>
  );
}
