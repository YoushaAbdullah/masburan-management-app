"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import Note from "@/components/Note";

interface NoteType {
  id: number;
  title: string;
  content: string;
  created_at: string;
}

interface NoteProps {
  note: NoteType;
  onDelete: (id: NoteType["id"]) => Promise<void>;
}

const NotesPage: React.FC = () => {
  const [notes, setNotes] = useState<NoteType[]>([]);
  const [content, setContent] = useState<string>("");
  const [title, setTitle] = useState<string>("");

  useEffect(() => {
    getNotes();
  }, []);

  const getNotes = async () => {
    try {
      const token = localStorage.getItem("accessToken"); // Retrieve the token from localStorage
      const response = await axios.get(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/notes/`,
        {
          headers: {
            Authorization: `Bearer ${token}`, // Include the token in the Authorization header
          },
        }
      );
      setNotes(response.data);
    } catch (error) {
      console.error("Error fetching notes:", error);
      alert("Failed to fetch notes.");
    }
  };

  const deleteNote = async (id: number) => {
    try {
      const token = localStorage.getItem("accessToken"); // Retrieve the token from localStorage
      const response = await axios.delete(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/notes/delete/${id}/`,
        {
          headers: {
            Authorization: `Bearer ${token}`, // Include the token in the Authorization header
          },
        }
      );
      if (response.status === 204) {
        alert("Note deleted!");
        getNotes();
      } else {
        alert("Failed to delete note.");
      }
    } catch (error) {
      console.error("Error deleting note:", error);
      alert("Failed to delete note.");
    }
  };

  const createNote = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("accessToken"); // Retrieve the token from localStorage
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/notes/`,
        { title, content },
        {
          headers: {
            Authorization: `Bearer ${token}`, // Include the token in the Authorization header
          },
        }
      );
      if (response.status === 201) {
        alert("Note created!");
        getNotes();
        setTitle("");
        setContent("");
      } else {
        alert("Failed to create note.");
      }
    } catch (error) {
      console.error("Error creating note:", error);
      alert("Failed to create note.");
    }
  };

  return (
    <div className="p-6">
      <div>
        <h2 className="text-2xl font-bold mb-4">Notes</h2>
        {notes.map((note) => (
          <Note note={note} onDelete={deleteNote} key={note.id} />
        ))}
      </div>
      <h2 className="text-2xl font-bold mt-8 mb-4">Create a Note</h2>
      <form onSubmit={createNote} className="flex flex-col gap-4">
        <div>
          <label htmlFor="title" className="block font-medium">
            Title:
          </label>
          <input
            type="text"
            id="title"
            name="title"
            required
            onChange={(e) => setTitle(e.target.value)}
            value={title}
            className="w-full p-2 border rounded"
          />
        </div>
        <div>
          <label htmlFor="content" className="block font-medium">
            Content:
          </label>
          <textarea
            id="content"
            name="content"
            required
            value={content}
            onChange={(e) => setContent(e.target.value)}
            className="w-full p-2 border rounded"
          ></textarea>
        </div>
        <button
          type="submit"
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default NotesPage;
