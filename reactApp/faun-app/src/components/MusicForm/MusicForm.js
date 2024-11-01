import { useState } from "react";
import { postMusic } from "../../services/musicServices";

export default function MusicForm(){
    
    const [audio, setAudio] = useState(null);
    const [data, setData] = useState({
        title: "",
        album: "",
        author: "",
        audio: null
    });

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setData((prevData) => ({
            ...prevData,
            [name]: value
        }));
    };

    const handleChange = (event) => {
        setAudio(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();

        formData.append("title", data.title);
        formData.append("album", data.album);
        formData.append("author", data.author);
        formData.append("audio", audio);

        try {
            const response = await postMusic(formData);
            console.log(response)
        } catch (error) {
            console.error("Error adding model:", error);
        }
    };


    return(
        <div>
            <div>
            <div>
                <div>title: </div>
                    <input name="title" onChange={handleInputChange} />
                </div>
                
                <div>
                    <div>author: </div>
                    <input name="author" onChange={handleInputChange} />
                </div>

                <div>
                    <div>album: </div>
                    <input name="album" onChange={handleInputChange} />
                </div>

                <div >
                    <label htmlFor="file-upload" >
                        <div>Upload Scaler</div>
                    </label>
                    <input id="file-upload" type="file" onChange={handleChange} />
                    
                </div>

                <button onClick={handleSubmit}>
                    Submit
                </button>

            </div>
        </div>
    )
}