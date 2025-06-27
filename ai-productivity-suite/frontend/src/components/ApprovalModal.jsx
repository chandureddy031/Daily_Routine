import React from 'react';

export default function ApprovalModal({ task, onApprove, onClose }) {
    return (
        <div className="modal">
            <div className="modal-content">
                <h3>Approve Task</h3>
                <p>{task.email_subject}</p>
                <button onClick={() => onApprove(task.$id)}>Approve</button>
                <button onClick={onClose}>Cancel</button>
            </div>
        </div>
    );
}