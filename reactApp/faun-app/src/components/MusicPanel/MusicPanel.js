export default function MusicPanel({ music }) {
    // Check if music is available
    if (!music) {
        return <div>No music data available.</div>;
    }

    return (
        <div>
            <label>Title:</label>
            <label>{music.title || 'Unknown Title'}</label>
    
            <label>Author:</label>
            <label>{music.author || 'Unknown Author'}</label>
        
            <label>Album:</label>
            <label>{music.album || 'Unknown Album'}</label>

            <audio controls>
                <source src={`data:audio/mpeg;base64,${music.audio}`} type="audio/mpeg" />
                Your browser does not support the audio element.
            </audio>

        </div>
    );
}
