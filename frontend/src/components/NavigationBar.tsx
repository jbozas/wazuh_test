import { Layout, Menu } from "antd";
import React from "react";
import { VideoCameraOutlined, UploadOutlined } from "@ant-design/icons";

import TasksTable from "../containers/tasks/Main";
import UsersTable from "../containers/users/Main";
import { BrowserRouter as Router, Link } from "react-router-dom";

const { Sider, Content } = Layout;

const menuOptions = {
  USERS: "1",
  TASKS: "2",
};

export default function NavigationBar() {
  var [selectedContent, setselectedContent] = React.useState(menuOptions.USERS);

  const onClickMenuItem = (e: any) => {
    setselectedContent(e.key);
  };

  return (
    <Layout style={{ minHeight: "inherit" }}>
      <Sider>
        <Router>
          <Menu
            theme="dark"
            mode="inline"
            defaultSelectedKeys={["1"]}
            onClick={onClickMenuItem}
          >
            <Menu.Item key={menuOptions.USERS} icon={<VideoCameraOutlined />}>
              <Link to="/users">Users</Link>
            </Menu.Item>
            <Menu.Item key={menuOptions.TASKS} icon={<UploadOutlined />}>
              <Link to="/tasks">Tasks</Link>
            </Menu.Item>
          </Menu>
        </Router>
      </Sider>
      <Layout className="site-layout">
        <Content
          className="site-layout-background"
          style={{
            margin: "24px 16px",
            padding: 24,
            minHeight: 280,
          }}
        >
          <UsersTable visible={selectedContent === menuOptions.USERS} />
          <TasksTable visible={selectedContent === menuOptions.TASKS} />
        </Content>
      </Layout>
    </Layout>
  );
}
