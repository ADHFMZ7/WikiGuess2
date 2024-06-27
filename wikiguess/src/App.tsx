import React from 'react';
import './App.css';

const App: React.FC = () => {
  return (
    <div className="content">
      <button className="box left-box">
        Left Box Content
      </button>

      <div className="center-content">
        <h1 className="title">Article Title</h1>
        <h2 className="score">Score: 0</h2>
        <span className="highscore">Highscore: 0</span>
      </div>

      <button className="box right-box">
        Right Box Content
      </button>
    </div>
  );
};

export default App;