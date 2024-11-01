import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AddMusicPage from './pages/AddMusicPage';
import ListMusicPage from './pages/ListMusicPage';
import PlayMusicPage from './pages/PlayMusicPage';
function App() {

  return (
    <div>
      <Router>
          <Routes>
            <Route path="/add" element={<AddMusicPage/>}/>
            <Route path="/list" element={<ListMusicPage/>}/>
            <Route path="/play" element={<PlayMusicPage/>}/>
          </Routes>
      </Router>
    </div>

  );
}

export default App;