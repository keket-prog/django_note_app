import React from "react";
import { Link } from "react-router-dom";

//trims the note to review just a title
let getTitle = (note) => {
  let title = note.body.split("\n")[0];

  if (title.length > 45) {
    return title.slice(0, 45);
  }
  return title;
};

//Display time on the note
let getTime = (note) => {
  return new Date(note.updated).toLocaleDateString();
};

const ListItem = ({ note }) => {
  return (
    <Link to={`/note/${note.id}`}>
      <div className="notes-list-item">
        <h3>{getTitle(note)}</h3>
        <p>{getTime(note)}</p>
      </div>
    </Link>
  );
};

export default ListItem;
