import { message } from 'antd';
import axios, { AxiosRequestConfig } from 'axios'
interface MyResponseType<T = any> {
    code: number;
    msg: string;
    data: T;
  }

const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000'
})

const request = async <T = any>(config: AxiosRequestConfig): Promise<MyResponseType<T>> => {
  try {
    const { data } = await instance.request<MyResponseType<T>>(config)
    // do something
    if (data.code === 0){
        return Promise.resolve(data);
    } else {
        throw new Error(data.msg)
    }
  } catch (err: any) {
    // do something
    message.error(err.message || 'server side exception')
    return Promise.reject(err);
  }
}

export default request;
