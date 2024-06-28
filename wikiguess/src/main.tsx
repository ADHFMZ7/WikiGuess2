import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

const articleInfo = {
  title: "Sample Article",
  leftContent: "This is the left box content for the sample article.",
  rightContent: "This is the right box content for the sample article.",
};

ReactDOM.render(
  <React.StrictMode>
    <App articleInfo={articleInfo} />
  </React.StrictMode>,
  document.getElementById('root')
);