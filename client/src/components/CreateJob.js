import React, { useState } from 'react';

function CreateJob({ onJobCreated }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [location, setLocation] = useState('');
  const [salary, setSalary] = useState('');

  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  };

  const handleLocationChange = (e) => {
    setLocation(e.target.value);
  };

  const handleSalaryChange = (e) => {
    setSalary(e.target.value);
  };

  const handleCreateJob = () => {
    // Validate the input data before creating the job
    if (!title || !description) {
      alert('Please enter a title and description for the job');
      return;
    }

    // Create the job object
    const newJob = {
      title,
      description,
      location,
      salary,
    };

    // Call the callback function to create the job
    onJobCreated(newJob);

    // Clear the input fields
    setTitle('');
    setDescription('');
    setLocation('');
    setSalary('');
  };

  return (
    <div className="max-w-md mx-auto bg-white p-6 rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold mb-4 text-center text-indigo-500">Create Job Listing</h2>
      <div className="mb-4 space-y-4">
        <div>
          <label htmlFor="title" className="block text-sm font-medium">Title:</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={handleTitleChange}
            className="mt-1 w-full px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>
        <div>
          <label htmlFor="description" className="block text-sm font-medium">Description:</label>
          <textarea
            id="description"
            value={description}
            onChange={handleDescriptionChange}
            className="mt-1 w-full px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>
        <div>
          <label htmlFor="location" className="block text-sm font-medium">Location:</label>
          <input
            type="text"
            id="location"
            value={location}
            onChange={handleLocationChange}
            className="mt-1 w-full px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>
        <div>
          <label htmlFor="salary" className="block text-sm font-medium">Salary:</label>
          <input
            type="text"
            id="salary"
            value={salary}
            onChange={handleSalaryChange}
            className="mt-1 w-full px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>
      </div>
      <button
        onClick={handleCreateJob}
        className="w-full bg-indigo-500 text-white font-semibold py-2 px-4 rounded hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      >
        Create Job
      </button>
    </div>
  );
}

export default CreateJob;
