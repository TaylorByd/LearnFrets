import React, { useEffect, useState } from "react";
import styled from "styled-components";

const Button = styled.button`
  background-color: #004d40;
  color: white;
  padding: 5px 28px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  margin: 0px 2px;
  transition: ease background-color 250ms;
  &:hover {
    background-color: #009688;
  }
`;

function App() {
  const [initialized, setInitialized] = useState(false); // State to track if initialization has occurred

  const buttonContent = (text) => {
    fetch("/selectednote", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: text,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data["bool"] === "True") {
          fetch("/correctnote");
        } else {
          fetch("/incorrectnote");
        }
        console.log(data);
      })
      .catch((error) => console.error("Error:", error));
  };

  useEffect(() => {
    if (!initialized) {
      // Only initialize if not already initialized
      fetch("/initialize")
        .then((res) => res.text())
        .then((message) => {
          console.log(message);
          setInitialized(true); // Set initialization to true after successful call
        })
        .catch((error) => console.error("Initialization failed:", error));
    }
  }, [initialized]); // Empty dependency array to only run on initial mount

  return (
    <div>
      <div>
        <style>{"body { background-color: #222831; }"}</style>
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            padding: "10px",
          }}
        >
          <img
            src={require("./images/modified_guitar_fretboard.png")}
            style={{ height: 117, width: 901 }}
            alt="Guitar Fretboard"
          />
        </div>
      </div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
        }}
      >
        {["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"].map(
          (note) => (
            <Button key={note} onClick={() => buttonContent(note)}>
              {note}
            </Button>
          )
        )}
      </div>
    </div>
  );
}

export default App;
