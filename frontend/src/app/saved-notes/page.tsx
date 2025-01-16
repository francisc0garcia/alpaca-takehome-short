"use client";

import Link from "next/link";
import { useState, useEffect } from "react";
import {Note} from "@/api_models"
import {loadNotesLoadNotesPost} from "@/api_public/api"
import moment from 'moment';


export default function SavedNotes() {
  const [notes, setNotes] = useState<Note[]>([]);

  useEffect(() => {
    // Load notes when first loading the page
    const loadNotes = async () => {
      // TODO: Add filters for start/end to page
      const response = await loadNotesLoadNotesPost({end_date: 0, start_date:0, therapist_id: "Some therapist id"});

      if (response.data.error) {
        alert("Error: " + response.data.error);
        return;
      }

      if (response.data.notes) {
        setNotes(response.data.notes);
      } else {
        alert("Error: No notes returned");
      }
    }
    loadNotes();

  }, [])

  // // This would typically fetch notes from an API
  // const mockNotes = [
  //   { id: 1, date: "2024-03-20", preview: "Patient presented with..." },
  //   { id: 2, date: "2024-03-19", preview: "Follow-up appointment for..." },
  // ];

  return (
    <div className="flex min-h-screen flex-col p-8 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Saved Notes</h1>
        <Link href="/" className="text-blue-600 hover:underline">
          Back to Home
        </Link>
      </div>

      <div className="space-y-4">
        {notes.map((note) => (
          <div key={note.id} className="p-4 border rounded-lg hover:bg-gray-50">
            <div className="flex justify-between items-center mb-2">
              <span className="font-semibold">Date: {`${moment.unix(note.date).fromNow()}`}</span>
              <button className="text-blue-600 hover:underline">
                View Full Note
              </button>
            </div>
            <p className="text-gray-600">{note.observations}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
