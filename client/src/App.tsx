import { useCallback, useRef, useState } from "react";

const RECORDING_LENGTH = 10_000;

const App = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [searchResult, setSearchResult] = useState<string | null>(null);
  const recorderRef = useRef<MediaRecorder | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  const startRecording = useCallback(async () => {
    setIsRecording(true);

    if (!navigator.mediaDevices) {
      console.error("recording not supported");
      return;
    }

    streamRef.current = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorderRef.current = new MediaRecorder(streamRef.current);

    recorderRef.current.ondataavailable = (e) => {
      chunksRef.current.push(e.data);
    };

    recorderRef.current.onstop = async () => {
      const form = new FormData();

      const blob = new Blob(chunksRef.current, { type: "audio/webm;codecs=opus" });
      const file = new File([blob], "recording.webm");

      form.append("file", file);

      const result = await fetch("/api/find", {
        method: "POST",
        body: form,
      });

      setSearchResult(await result.text());

      recorderRef.current = null;
      streamRef.current = null;
      chunksRef.current = [];
    };

    recorderRef.current.start();
    setTimeout(() => {
      recorderRef.current?.stop();
      setIsRecording(false);
    }, RECORDING_LENGTH);
  }, []);

  return (
    <>
      <button onClick={startRecording}></button>
      <div className="progress-bar">
        <div
          className={`progress-bar-fill ${isRecording && "active"}`}
          style={{
            transition: isRecording ? `linear ${RECORDING_LENGTH / 1000}s` : "none",
          }}
        />
      </div>
      <div>
        <p>{searchResult}</p>
      </div>
    </>
  );
};

export default App;
