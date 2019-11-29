import {GET_TOTALNAMA} from '../actions/types'

const initialState = {
    totalnama: []
}
export default function(state = initialState,action){
    switch(action.type){
        case GET_TOTALNAMA:
            return{
                ...state,
                totalnama: action.payload
            }
        default:
            return state;
    }
}