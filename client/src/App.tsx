import { useEffect, useState } from "react";

const App = () => {
  const [message, setMessage] = useState("Loading...");

  const fetchServer = async () => {
    const response = await fetch("/api");
    setMessage(await response.text());
  };

  useEffect(() => {
    fetchServer();
  });

  return <div>{message}</div>;
};

export default App;
