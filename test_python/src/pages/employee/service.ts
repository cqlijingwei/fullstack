import { ListItem } from ".";
import request from "../../util/request";

export const editAction = (data: {[key: string]: unknown}) => {
    return request({
        url: '/api/user/edit',
        method: 'POST',
        data,
    })
}

export const createEmployeeAction = (data: {[key: string]: unknown}) => {
    return request({
        url: '/api/user/add',
        method: 'POST',
        data: data
    })
}

export const deleteAction = (id: number) => {
    return request({
        url: '/api/user/del',
        method: 'POST',
        data: {userid: id},
    })
}

export const getListAction = (params: {
    page?: number;
    pageSize?: number;
    firstName?: string;
    lastName?: string;
    salary?: number
}) => {
    return request<{
        employees: ListItem[];
        total: number;
    }>({
        method: 'GET',
        url: '/api/user/search',
        params: {
            current_page: params.page,
            page_size: params.pageSize,
        },
    })
}

