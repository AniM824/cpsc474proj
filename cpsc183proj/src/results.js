import React from "react";

const Results = ({ answers, goToHome }) => {
  // Reasonings for each question
  const reasonings = [
    {
      agree: "yayayaya1",
      disagree: "nononono1",
    },
    {
      agree: "yayayaya2",
      disagree: "nononono2",
    },
    {
      agree: "yayayaya3",
      disagree: "nononono3",
    },
    {
      agree: "yayayaya4",
      disagree: "nononono4",
    },
    {
      agree: "yayayaya5",
      disagree: "nononono5",
    },
    {
      agree: "yayayaya6",
      disagree: "nononono6",
    },
    {
      agree: "yayayaya7",
      disagree: "nononono7",
    },
    {
      agree: "yayayaya8",
      disagree: "nononono8",
    },
  ];

  // Scoring system
  const getScore = (answer) => {
    switch (answer) {
      case "Strongly Disagree":
        return -2;
      case "Disagree":
        return -1;
      case "Agree":
        return 1;
      case "Strongly Agree":
        return 2;
      default:
        return 0;
    }
  };

  // Calculate the overall score
  const totalScore = answers.reduce((sum, q) => sum + getScore(q.answer), 0);

  // Determine prediction based on score
  const prediction = totalScore > 0 ? "agree" : "disagree";

  // Generate the reasoning paragraph
  const reasoningParagraph = answers
    .map((q, idx) => {
      const isAgree = getScore(q.answer) > 0;
      // Only include reasoning if the answer aligns with the final prediction
      if (
        (prediction === "agree" && isAgree) ||
        (prediction === "disagree" && !isAgree)
      ) {
        return isAgree ? reasonings[idx].agree : reasonings[idx].disagree;
      }
      return null;
    })
    .filter(Boolean) // Remove null values
    .join(" ");

  return (
    <div
      style={{
        fontFamily: "'Poppins', sans-serif",
        textAlign: "center",
        padding: "20px",
        lineHeight: "1.8",
      }}
    >
      <h1 style={{ fontSize: "2.5rem", color: "#276749" }}>Results</h1>
      <p style={{ fontSize: "1.8rem", marginTop: "20px" }}>
        Based on your answers, we predict that you <strong>{prediction}</strong>{" "}
        with the scenario.
      </p>
      <div
        style={{
          margin: "40px auto",
          padding: "20px",
          maxWidth: "800px",
          backgroundColor: "#f9f9f9",
          border: "1px solid #ddd",
          borderRadius: "5px",
          textAlign: "left",
        }}
      >
        <h2 style={{ fontSize: "2rem", color: "#007B83" }}>Justification</h2>
        <p style={{ fontSize: "1.4rem" }}>{reasoningParagraph}</p>
      </div>
      <button
        onClick={goToHome}
        style={{
          marginTop: "30px",
          padding: "15px 30px",
          fontSize: "1.5rem",
          backgroundColor: "#276749",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Go to Home
      </button>
    </div>
  );
};

export default Results;
