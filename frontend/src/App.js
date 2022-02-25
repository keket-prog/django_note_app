import "./App.css";
import { Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import NotesListPage from "./pages/NotesListPage";
import NotePage from "./pages/NotePage";
function App() {
  return (
    <div className="container dark">
      <div className="app">
        <Header />
        <Routes>
          <Route path="/" exact element={<NotesListPage />} />
          <Route path="/note/:id" exact element={<NotePage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
