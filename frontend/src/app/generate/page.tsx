"use client";

import { useState } from "react";
import Link from "next/link";

export default function GenerateNote() {
  const [observations, setObservations] = useState("");
  const [generatedNote, setGeneratedNote] = useState("");

  const handleGenerate = async () => {
    // TODO: Implement API call to generate note
    setGeneratedNote("Generated note will appear here...");
  };

  const handleSave = async () => {
    // TODO: Implement save functionality
    alert("Save functionality to be implemented");
  };

  return (
    <div className="flex min-h-screen flex-col p-8 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Generate Note</h1>
        <Link href="/" className="text-blue-600 hover:underline">
          Back to Home
        </Link>
      </div>

      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Patient Observations
          </label>
          <textarea
            className="w-full h-48 p-4 border rounded-lg"
            placeholder="Enter your observations here..."
            value={observations}
            onChange={(e) => setObservations(e.target.value)}
          />
        </div>

        <button
          onClick={handleGenerate}
          className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700"
        >
          Generate Note
        </button>

        {generatedNote && (
          <div className="mt-8">
            <h2 className="text-xl font-semibold mb-4">Generated Note</h2>
            <div className="p-4 border rounded-lg bg-gray-50">
              <p>{generatedNote}</p>
            </div>
            <button
              onClick={handleSave}
              className="mt-4 bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700"
            >
              Save Note
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
