import React, { useState } from 'react';
import Home from './home';
import Results from './results';

const App = () => {
  const [page, setPage] = useState('home');
  const [answers, setAnswers] = useState([]);

  const handleSubmit = (answers) => {
    setAnswers(answers);
    setPage('results');
  };

  const goToHome = () => {
    setAnswers([]);
    setPage('home');
  };

  return (
    <div>
      {page === 'home' ? (
        <Home onSubmit={handleSubmit} />
      ) : (
        <Results answers={answers} goToHome={goToHome} />
      )}
    </div>
  );
};

export default App;
