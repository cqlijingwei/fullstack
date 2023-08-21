import React, { useEffect, useState } from "react";

import {
  Button,
  Form,
  FormInstance,
  Input,
  InputNumber,
  Modal,
  Space,
  Table,
} from "antd";
import styles from "./index.module.css";
import { createEmployeeAction, deleteAction, editAction, getListAction } from "./service";

export interface ListItem {
  userid: number;
  firstName: string;
  lastName: string;
  salary: number;
}
enum OperationTypeEnum {
    EDIT,
    CREATE,
}
const EmployeeManagement = () => {
  const [dataSource, setDataSource] = useState<ListItem[]>([{
    userid: 1,
    firstName: 'ksdf',
    lastName: 'sdf',
    salary: 100,
  }]);
  const [visible, setVisible] = useState(false);
  const [loading, setLoading] = useState(false);
  const [operatonType, setOperationType] = useState<OperationTypeEnum>();
  const [confirmLoading, setConfirmLoading] = useState(false);
  const [pageSize, setPageSize] = useState(10);
  const [current, setCurrent] = useState(1);
  const [total, setTotal] = useState(0);
  const [form] = Form.useForm<FormInstance>();
  const [editId, setEidtItemId] = useState<number | null>(null);

  const formItemLayout = {
    labelCol: {
      xs: { span: 24 },
      sm: { span: 6 },
    },
    wrapperCol: {
      xs: { span: 24 },
      sm: { span: 14 },
    },
  };

  const handleDelete = async (id: number) => {
     Modal.confirm({
        title: 'Delete',
        content: 'Are you sure you want to delete the current dataSource',
        async onOk(){
            await deleteAction(id);
            fetchList({
                pageSize,
                page: current,
            })
        }
     })
  };

  const handleEdit = (item: any) => {
    setVisible(true);
    setOperationType(OperationTypeEnum.EDIT);
    setEidtItemId(item.userid);
    form.setFieldsValue({
      ...item,
    });
  };

  const fetchList = async (params: {
    pageSize: number;
    page: number;
    firstName?: string;
    lastName?: string;
    slary?: number;
  }) => {
    try {
      setLoading(true);
      const { data } = await getListAction(params);
      setDataSource(data.employees);
      setTotal(data.total);
    } catch (err) {
      console.log("network error", err);
    } finally {
        setLoading(false);
    }
  };
  const header = [
    {
      title: "First Name",
      dataIndex: "firstName",
      key: "firstName",
    },
    {
      title: "Last Name",
      dataIndex: "lastName",
      key: "lastName",
    },
    {
      title: "Salary",
      dataIndex: "salary",
      key: "salary",
    },
    {
      key: "operations",
      render: (record: ListItem) => {
        return (
          <Space>
            <Button
              type="text"
              style={{
                color: "orange",
              }}
              onClick={() => handleEdit(record)}
            >
              编辑
            </Button>
            <Button
              type="text"
              style={{
                color: "red",
              }}
              onClick={() => handleDelete(record.userid)}
            >
              删除
            </Button>
          </Space>
        );
      },
    },
  ];

  const handleConfirm = async () => {
    await form.validateFields();
    const formValues = form.getFieldsValue() as any;
    try {
        setConfirmLoading(true);
        if (operatonType === OperationTypeEnum.CREATE){
            await createEmployeeAction(formValues);
        } else if (operatonType === OperationTypeEnum.EDIT){
            await editAction({
                userid: editId,
                ...formValues
            });
        }
        setVisible(false);
        fetchList({
            page: current,
            pageSize,
        })
    } finally{
        setConfirmLoading(false);
    }
  };

  const handleCreate = async () => {
    setVisible(true);
    setOperationType(OperationTypeEnum.CREATE);
    form.resetFields();
  }
  useEffect(() => {
    fetchList({
        page: current,
        pageSize,
    })
  }, []);
  

  return (
    <div className={styles.container}>
      <div className={styles.main}>
        <div className={styles.title}>

         <h2 >EMPLOYEES</h2>
         <Button type="primary" onClick={()=> handleCreate()}>Create</Button>
        </div>
        <div>
          <div className={styles.listBody} id="scrollableDiv">
            <Table
              columns={header}
              dataSource={dataSource}
              loading={loading}
              pagination={{
                pageSize: pageSize,
                current: current,
                total: total,
                onChange(_page, _pageSize) {
                  setPageSize(_pageSize);
                  setCurrent(_page);
                  fetchList({
                    pageSize: _pageSize,
                    page: _page,
                  });
                },
              }}
            />
          </div>
        </div>
      </div>
      <Modal
        open={visible}
        title={operatonType === OperationTypeEnum.CREATE ? 'Create' : 'Edit'}
        onCancel={() => setVisible(false)}
        onOk={handleConfirm}
        confirmLoading={confirmLoading}
      >
        <Form {...formItemLayout} form={form}>
          <Form.Item
            name="firstName"
            label="First Name"
            required
            rules={[
              {
                required: true,
              },
            ]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="lastName"
            label="Lirst Name"
            required
            rules={[
              {
                required: true,
              },
            ]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="salary"
            label="Salary"
            required
            rules={[
              {
                required: true,
              },
            ]}
          >
            <InputNumber />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default EmployeeManagement;
