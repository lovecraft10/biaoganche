import axios from 'axios';

let base = 'http://127.0.0.1:5000/api';

export const requestLogin = params => {
    return axios({
        method: 'POST',
        url: `${base}/login`,
        auth: params
    })
    .then(res => res.data);
};

export const setpwd = params => {
    return axios.post(`${base}/setpwd`, params);
};

export const getUserListPage = params => {
    return axios.get(`${base}/users/listpage`, { params: params });
};
export const getDoorPage = params => {
    return axios.get(`${base}/users/doorpage`, { params: params });
};
export const getTripPage = params => {
    return axios.get(`${base}/users/trippage`, { params: params });
};
export const removeUser = params => {
    return axios.get(`${base}/user/remove`, { params: params });
};

export const batchRemoveUser = params => {
    return axios.get(`${base}/user/bathremove`, { params: params });
};

export const getdrawPieChart = () => {
    return axios.get(`${base}/getdrawPieChart`);
};
export const getdrawPieChart1 = () => {
    return axios.get(`${base}/getdrawPieChart1`);
};

export const getdrawLineChart = () => {
    return axios.get(`${base}/getdrawLineChart`);
};

export const getdrawLineChart1 = () => {
    return axios.get(`${base}/getdrawLineChart1`);
};

export const TIMEandFUEL = params => {
    return axios.get(`${base}/getTimeandFuel`, { params: params });
};

export const getCarMap= params => {
    return axios.get(`${base}/getCarMap`);
};

