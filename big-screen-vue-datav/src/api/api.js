import axios from '@/utils/axios'


export const GETMONEY = params => {
    return axios.get(`/api/getMoney`, { params: params });
};

export const GETBOOK = params => {
    return axios.get(`/api/getBook`, { params: params });
};
