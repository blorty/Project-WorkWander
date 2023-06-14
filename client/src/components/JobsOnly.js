import React, { useEffect, useState } from 'react';
import 'tailwindcss/tailwind.css';

function JobsOnly() {
    const [jobs, setJobs] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        fetch('/jobs')
            .then((response) => response.json())
            .then((data) => setJobs(data))
            .catch((error) => console.log(error));
    }, []);


    const handleSearch = (e) => {
        setSearchTerm(e.target.value);
    };

    const filteredJobs = jobs.filter((job) =>
        (job.title || '').toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div className="bg-gradient-animation min-h-screen flex flex-col justify-start items-center">
        <div className="mt-8 text-center">
            <div className="mb-4">
            <input
                type="text"
                placeholder="Search for jobs"
                className="px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-500"
                value={searchTerm}
                onChange={handleSearch}
            />
            </div>
            {filteredJobs.map((job) => (
            <div key={job.id} className="bg-white rounded shadow p-4 m-4">
                <h2 className="text-xl font-bold">{job.title}</h2>
                <p className="text-gray-600 mb-2">{job.description}</p>
                <p className="text-gray-600 mb-2">{job.location}</p>
                <p className="text-gray-600 mb-2">{`$${job.salary}`}</p>
            </div>
            ))}
        </div>
        </div>
    );
}

export default JobsOnly;