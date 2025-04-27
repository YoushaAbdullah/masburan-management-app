"use client";

import React from "react";

type NoteType = {
  id: number | string;
  title: string;
  content: string;
  created_at: string;
};

interface NoteProps {
  note: NoteType;
  onDelete: (id: NoteType["id"]) => void;
}

export default function Note({ note, onDelete }: NoteProps) {
  const formattedDate = new Date(note.created_at).toLocaleDateString("en-US");

  return (
    <div className="note-container max-w-sm bg-white shadow-md rounded-2xl p-6 mb-4">
      <p className="note-title text-xl font-semibold text-gray-800 mb-2">
        {note.title}
      </p>
      <p className="note-content text-gray-700 mb-4 whitespace-pre-wrap">
        {note.content}
      </p>
      <p className="note-date text-sm text-gray-500">{formattedDate}</p>
      <button
        className="delete-button px-3 py-1 bg-red-500 hover:bg-red-600 text-white rounded-lg transition"
        onClick={() => onDelete(note.id)}
      >
        Delete
      </button>
    </div>
  );
}
