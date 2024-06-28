import React from 'react';
import './App.css';

interface ArticleInfo {
  title: string;
  leftContent: string;
  rightContent: string;
}

interface AppProps {
  articleInfo: ArticleInfo;
}

const App: React.FC<AppProps> = ({ articleInfo }) => {
  return (
    <div className="content">
      <button className="box left-box">
        {articleInfo.leftContent}
      </button>
      <div className="center-content">
        <h1 className="title">{articleInfo.title}</h1>
        <h2 className="score">Score: 0</h2>
        <span className="highscore">Highscore: 0</span>
      </div>
      <button className="box right-box">
        {articleInfo.rightContent}
      </button>
    </div>
  );
};

export default App;