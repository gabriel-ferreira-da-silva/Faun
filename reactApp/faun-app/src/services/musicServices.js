import axios from 'axios'

export const fetchAllMusic = async ()=>{
    try{
        const response = await axios.get("http://localhost:5000/api/music")
        return response.data
    }catch(error){
        throw error
    }
};

export const postMusic = async (data)=>{
    try{
        const response = await axios.post("http://localhost:5000/api/music/add",data)
        return response.data
    }catch(error){
        throw error
    }
};


