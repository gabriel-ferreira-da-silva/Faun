import MusicPanel from "../MusicPanel/MusicPanel";
import { fetchAllMusic } from "../../services/musicServices";
import { useEffect, useState } from "react";
import style from './style.module.css'

export default function ListMusicPanel() {
    const [musics, setMusics] = useState([]);

    useEffect(() => {
        const fetchAll = async () => {
            try {
                const response = await fetchAllMusic();
                console.log(response);
                setMusics(response);
            } catch (error) {
                console.error("Error fetching music data:", error);
            }
        };
        
        fetchAll(); 
    }, []);

    return (
        <div className={style.container}>
            {musics.map((music, index) => (
                <div key={index}>
                    <MusicPanel music={music} />
                </div>
            ))}
        </div>
    );
}
