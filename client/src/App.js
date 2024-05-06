import React, { useEffect, useState } from "react";
import styled from "styled-components";

const Button = styled.button`
  background-color: #004d40;
  color: white;
  padding: 5px 15px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  box-shadow: 0px 2px 2px lightgray;
  margin: 0px 2px;
  transition: ease background-color 250ms;
  &:hover {
    background-color: #009688;
  }
`;

function App() {
  const buttonContent = (text) => {
    fetch("/selectednote", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: text,
    });
    setbuttonText(text);
  };

  const [matchedNote, setmatchedNote] = useState([{}]);
  const [buttonText, setbuttonText] = useState("0");
  const [matchedNoteColor, setmatchedNoteColor] = useState("black");

  useEffect(() => {
    fetch("/correctnote")
      .then((res) => res.json())
      .then((matchedNote) => {
        setmatchedNote(matchedNote);
        if (matchedNote["bool"] === "True") {
          setmatchedNoteColor("green");
        } else {
          setmatchedNoteColor("red");
        }
        console.log(matchedNote);
      });
  }, [buttonText]);

  return (
    <div>
      <p style={{ color: matchedNoteColor }}>{matchedNote["bool"]}</p>
      <div>
        <img
          src={require("./images/GuitarFretboard.png")}
          style={{ height: 117, width: 901 }}
        />
      </div>
      <Button onClick={() => buttonContent("C")}>C</Button>
      <Button onClick={() => buttonContent("C#")}>C#</Button>
      <Button onClick={() => buttonContent("D")}>D</Button>
      <Button onClick={() => buttonContent("D#")}>D#</Button>
      <Button onClick={() => buttonContent("E")}>E</Button>
      <Button onClick={() => buttonContent("F")}>F</Button>
      <Button onClick={() => buttonContent("F#")}>F#</Button>
      <Button onClick={() => buttonContent("G")}>G</Button>
      <Button onClick={() => buttonContent("G#")}>G#</Button>
      <Button onClick={() => buttonContent("A")}>A</Button>
      <Button onClick={() => buttonContent("A#")}>A#</Button>
      <Button onClick={() => buttonContent("B")}>B</Button>
    </div>
  );
}

export default App;
