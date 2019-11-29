import axios from "axios";

import {GET_TOTALNAMA} from './types';

//GET Nama
export const getTotalnama = nama => dispatch =>{
     axios
     .get(`/total/${nama}/`)
        .then(res =>{
            dispatch({
                type: GET_TOTALNAMA,
                payload: res.data
            });
     }).catch(err => Console.log(err));
}