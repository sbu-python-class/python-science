// Save dropdown states before navigation
function saveDropdownStates() {
  const states = {};
  let index = 0;

  // Save states for details-based dropdowns (Sphinx Design, toggle-details, etc.)
  document.querySelectorAll('details.dropdown, details.sd-dropdown, details.toggle-details').forEach((detail) => {
    const id = detail.id || `details-dropdown-${index++}`;
    states[id] = detail.open;
  });

  // Save states for div-based dropdowns (admonitions with toggle buttons)
  index = 0;
  document.querySelectorAll('div.dropdown').forEach((div) => {
    const id = div.id || `div-dropdown-${index++}`;
    const isOpen = !div.classList.contains('toggle-hidden');
    states[id] = isOpen;
  });

  sessionStorage.setItem('dropdownStates', JSON.stringify(states));
}

// Restore dropdown states after page load
function restoreDropdownStates() {
  const savedStates = sessionStorage.getItem('dropdownStates');
  if (!savedStates) return;
  
  try {
    const states = JSON.parse(savedStates);
    let index = 0;

    // Restore states for details-based dropdowns
    document.querySelectorAll('details.dropdown, details.sd-dropdown, details.toggle-details').forEach((detail) => {
      const id = detail.id || `details-dropdown-${index++}`;
      const shouldBeOpen = states[id];
      
      if (shouldBeOpen !== undefined && detail.open !== shouldBeOpen) {
        detail.open = shouldBeOpen;
      }
    });

    // Restore states for div-based dropdowns
    index = 0;
    document.querySelectorAll('div.dropdown').forEach((div) => {
      const id = div.id || `div-dropdown-${index++}`;
      const shouldBeOpen = states[id];
      
      if (shouldBeOpen !== undefined) {
        const isCurrentlyOpen = !div.classList.contains('toggle-hidden');
        
        // Toggle if the state doesn't match
        if (shouldBeOpen !== isCurrentlyOpen) {
          const title = div.querySelector('.admonition-title');
          if (title) {
            title.click();
          }
        }
      }
    });
  } catch (e) {
    console.error('Error restoring dropdown states:', e);
  }
}

// Save states when clicking on internal links
document.addEventListener('click', function(e) {
  const link = e.target.closest('a');
  if (link && link.origin === window.location.origin) {
    saveDropdownStates();
  }
});

// Save states before navigating away
window.addEventListener('beforeunload', function() {
  saveDropdownStates();
});

// Restore dropdown states on page load
window.addEventListener("load", function() {
  restoreDropdownStates();
});
