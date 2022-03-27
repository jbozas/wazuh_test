import React from 'react';
import './App.css';
import GenericTable from "./components/Table";
import NavigationBar from "./components/NavigationBar";
import Menu from "./components/Menu";

export default function App() {
  const dummy_dataSource = [
    {
      key: '1',
      name: 'Mike',
      username: 'mikeulligan',
      email: 'mike@gmail.com',
      address: 'avenue 14512',
      website: 'asdasd@.com',
    },
    {
      key: '2',
      name: 'John',
      username: 'johncarpenter',
      email: 'jhon@gmail.com',
      address: 'avenue 14512',
      website: 'asdasd@.com',
    },
  ];

  const dummy_columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Username',
      dataIndex: 'username',
      key: 'username',
    },
    {
      title: 'Email',
      dataIndex: 'email',
      key: 'email',
    },
  ];

return <div className="App">
    <NavigationBar/>
  </div>
}
