import React, { useState, useEffect, useContext } from "react";
import { Link, useParams, useHistory } from "react-router-dom";
import { Context } from "../store/appContext";

export const AppFeed = (props) => {
  //react declarations
  const history = useHistory();
  const { store, actions } = useContext(Context);
  const params = useParams();

  //declare states here vvvv
  const [state, setState] = useState("State");

  return (
    <div className="dashBody w-100">
      <div className="dashBoardHome">
        ADD PAGE CONTENT HERE!!!!!!!!!!!!!!!!!!!!!!!!!
      </div>
    </div>
  );
};
