import axios from '@/utils/axios'

export const GETMONEY = params => {
    return axios.get(`/api/getMoney`, { params: params });
};
export const GETBOOK = params => {
    return axios.get(`/api/getBook`, { params: params });
};
export const GETCOUNT = params => {
    return axios.get(`/api/getCount`, { params: params });
};
export const GETYEAR = params => {
    return axios.get(`/api/getYear`, { params: params });
};
export const GETBRAND = params => {
    return axios.get(`/api/getBrand`, { params: params });
};
