import React, { useEffect, useState } from "react";
import useFetch from "../useFetch";
import GenericTable from "../../components/Table";
import { Input, Button } from "antd";
import { ENDPOINT } from "./constants";

interface tableProps {
  visible: boolean;
}

export default function Main({ visible }: tableProps) {
  var [data, setData] = useState(null);
  // interface Task {
  //   id: number;
  //   user_id: string;
  //   title: string;
  //   completed: boolean;
  // }
  useEffect(() => {
    if (!data) {
      fetch("http://127.0.0.1:5000/tasks")
        .then((data) => {
          return data.json();
        })
        .then((data) => {
          setData(data.data);
        })
        .catch((err) => {
          console.log("error fetching api");
        });
    }
  }, []);

  function handleFilter(e: any) {
    const input = document.querySelector(".ant-input");

    fetch(`http://127.0.0.1:5000/tasks?user_id=${input?.getAttribute("value")}`)
      .then((data) => {
        return data.json();
      })
      .then((data) => {
        setData(data.data);
      });
  }

  function handleResetFilter(e: any) {
    fetch("http://127.0.0.1:5000/tasks")
      .then((data) => {
        return data.json();
      })
      .then((data) => {
        setData(data.data);
      })
      .catch((err) => {
        console.log("error fetching api");
      });
  }

  const columns = [
    {
      title: "Title",
      dataIndex: "title",
      key: "title",
    },
    {
      title: "User ID",
      dataIndex: "user_id",
      key: "user_id",
    },
    {
      title: "Completed",
      dataIndex: "completed",
      key: "completed",
      filters: [
        { text: "Yes", value: true },
        { text: "No", value: false },
      ],
      onFilter: (value: boolean, record: any) => record.completed === value,
      render: (completed: boolean) => (completed ? "Yes" : "No"),
    },
  ];

  return (
    <>
      {visible ? (
        <div>
          <div>
            <Input.Group compact>
              <Input
                type="number"
                style={{ width: "calc(100% - 800px)", textAlign: "left" }}
              />
              <Button onClick={handleFilter} type="primary">
                Filter by user ID
              </Button>
              <Button onClick={handleResetFilter} type="primary">
                Reset filters
              </Button>
            </Input.Group>
          </div>
          {data && <GenericTable dataSource={data} columns={columns} />}
        </div>
      ) : null}
    </>
  );
}
