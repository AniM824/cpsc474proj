import React, { useState } from "react";

const Home = ({ onSubmit }) => {
  const [questions, setQuestions] = useState([
    {
      id: 1,
      prompt: "Authors Guild v. Google (2015)",
      description:
        "Google digitized millions of books for its Google Books search engine, allowing users to search text and view small snippets of copyrighted works. The Authors Guild argued this violated copyright law, while Google claimed it was transformative and beneficial for research and education. The court ruled in favor of Google, holding that its snippet display was fair use because it was transformative and did not harm the market for the original works.",
      answer: "",
    },
    {
      id: 2,
      prompt: "Google LLC v. Oracle America, Inc. (2021)",
      description:
        "Google used 11,500 lines of Java API code to develop its Android platform, arguing this use was necessary for innovation and fell under fair use. Oracle, the owner of the Java API, claimed copyright infringement, stating Google’s use was not transformative. The Supreme Court sided with Google, concluding that its use was fair because it was transformative, limited in scope, and did not harm Oracle's market.",
      answer: "",
    },
    {
      id: 3,
      prompt: "Bloomberg v. Swatch Group (2014)",
      description:
        "Swatch held a private earnings call for analysts and later released a transcript. Bloomberg published the entire audio recording, claiming it was essential for news reporting. Swatch sued for copyright infringement, arguing the recording was not intended for public use. The court ruled in favor of Bloomberg, stating that the full reproduction was fair use due to its transformative purpose of news dissemination.",
      answer: "",
    },
    {
      id: 4,
      prompt: "Warner Bros. Entertainment Inc. v. RDR Books (2008)",
      description:
        "This case revolved around The Harry Potter Lexicon, a fan-created encyclopedia based on J.K. Rowling’s Harry Potter series. The author and Warner Bros. sued RDR Books, arguing that the Lexicon infringed on their copyrights by copying substantial portions of the books without permission. The court ruled in favor of Warner Bros., restricting the Lexicon’s publication due to its commercial nature and market harm.",
      answer: "",
    },
    {
      id: 5,
      prompt: "Sony Corp. v. Universal City Studios (1984)",
      description:
        "Universal sued Sony over the Betamax VCR, claiming it enabled users to record copyrighted TV programs, leading to widespread copyright infringement. Sony argued the device had substantial non-infringing uses, such as time-shifting (recording programs for later viewing). The Supreme Court ruled in favor of Sony, establishing the \"substantial non-infringing use\" doctrine and holding that manufacturers cannot be held liable for copyright infringement by their customers if the product has significant lawful applications.",
      answer: "",
    },
    {
      id: 6,
      prompt: "Question 6",
      description: "You feel comfortable taking risks.",
      answer: "",
    },
    {
      id: 7,
      prompt: "Question 7",
      description: "You adapt easily to change.",
      answer: "",
    },
    {
      id: 8,
      prompt: "Question 8",
      description: "You prefer structure over spontaneity.",
      answer: "",
    },
  ]);

  const allAnswered = questions.every((q) => q.answer !== "");

  const handleAnswerChange = (id, answer) => {
    setQuestions(
      questions.map((q) => (q.id === id ? { ...q, answer } : q))
    );
  };

  const handleSubmit = () => {
    if (allAnswered) {
      onSubmit(questions);
    }
  };

  return (
    <div
      style={{
        fontFamily: "'Poppins', sans-serif",
        color: "#333",
        lineHeight: "1.8",
        margin: "0",
        padding: "0",
      }}
    >
      {/* Top Bar */}
      <div
        style={{
          backgroundColor: "#007B83",
          color: "white",
          padding: "15px 0",
          fontSize: "1.8rem",
          textAlign: "center",
          position: "sticky",
          top: 0,
          zIndex: 1000,
        }}
      >
        CPSC 183 Final Project
      </div>

      {/* Banner */}
      <div
        style={{
          backgroundColor: "#4CAF50",
          color: "white",
          padding: "30px",
          textAlign: "center",
        }}
      >
        <h1 style={{ fontSize: "2.5rem", margin: "0 0 10px" }}>
          A Personality Quiz on Copyright
        </h1>
        <p style={{ fontSize: "2rem", margin: "0" }}>
          A political advocacy group leverages an AI model trained on a dataset
          containing copyrighted books, movies, and social media posts to
          generate memes and short videos. These creations are designed to
          critique political candidates and policies. The group disseminates
          these memes and videos on platforms like TikTok, pairing iconic movie
          scenes, dialogue, or music with political messages. The campaign
          becomes massively influential, with millions of views shaping public
          opinion. However, the campaign is monetized through sponsorships and
          ad revenue.
        </p>
      </div>

      {/* Secondary Header */}
    <div
    style={{
        backgroundColor: "#FFC107", // Yellow-like color for contrast
        color: "#333",
        padding: "30px",
        textAlign: "center",
    }}
    >
    <p style={{ fontSize: "1.8rem", margin: "0", lineHeight: "1.6" }}>
        Please answer the following questions to help us explore how your opinions on
        landmark legal cases, ethical dilemmas, and societal values may predict your
        perspective on the given scenario. By examining your views on copyright, free
        speech, monetization, and innovation, we aim to understand how these
        principles shape your stance on the evolving role of AI in participatory
        culture and political discourse.
    </p>
    </div>


      {/* Questions Section */}
      <div style={{ padding: "30px", fontSize: "1.6rem", margin: "0 auto", maxWidth: "1200px" }}>
        {questions.map((q) => (
          <div
            key={q.id}
            style={{
              marginBottom: "40px",
              borderBottom: "1px solid #ccc",
              paddingBottom: "40px",
            }}
          >
            {/* Court Case/Question Header */}
            <h2
              style={{
                fontWeight: "bold",
                fontSize: "2rem",
                marginBottom: "10px",
                textAlign: "center",
              }}
            >
              {q.prompt}
            </h2>
            {/* Description */}
            <p style={{ fontSize: "1.6rem", textAlign: "center" }}>
              {q.description}
            </p>

            {/* Answer Options */}
            <div
              style={{
                display: "flex",
                justifyContent: "center",
                marginTop: "20px",
                border: "1px solid gray",
                borderRadius: "5px",
                overflow: "hidden",
              }}
            >
              {["Strongly Disagree", "Disagree", "Agree", "Strongly Agree"].map(
                (option, idx) => (
                  <button
                    key={option}
                    style={{
                      padding: "20px",
                      border: "none",
                      backgroundColor:
                        q.answer === option ? "#d0eaff" : "#f0f0f0",
                      cursor: "pointer",
                      flex: 1,
                      fontSize: "1.6rem",
                      fontWeight: "500",
                      borderLeft:
                        idx === 0 ? "none" : "1px solid #ccc", // Only add borders between buttons
                      transition: "background-color 0.3s, border 0.3s",
                    }}
                    onClick={() => handleAnswerChange(q.id, option)}
                    onMouseEnter={(e) =>
                      (e.target.style.backgroundColor = "#e0e0e0")
                    }
                    onMouseLeave={(e) =>
                      (e.target.style.backgroundColor =
                        q.answer === option ? "#d0eaff" : "#f0f0f0")
                    }
                  >
                    {option}
                  </button>
                )
              )}
            </div>
          </div>
        ))}

        {/* Submit Button */}
        <div style={{ textAlign: "center", marginTop: "50px" }}>
          <button
            disabled={!allAnswered}
            onClick={handleSubmit}
            style={{
              padding: "20px 40px",
              fontSize: "1.8rem",
              cursor: allAnswered ? "pointer" : "not-allowed",
              backgroundColor: allAnswered ? "#4CAF50" : "#ccc",
              color: "white",
              border: "none",
              borderRadius: "5px",
            }}
          >
            Submit
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;
