import axios from '@/utils/axios'


export const GETMONEY = params => {
    return axios.get(`/api/getMoney`, { params: params });
};
