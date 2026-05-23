 
        'use strict';

        //Toggle Function
        const elemToggleFunc = function(elem) { elem.classList.toggle('active'); }

        // Header Sticky & Go-Top
        const header = document.querySelector('[data-header]');
        const goTopBtn = document.querySelector('[data-go-top]');
        window.addEventListener('scroll', function(){ 
            if(window.scrollY >= 10) { 
                header.classList.add('active'); 
                goTopBtn.classList.add('active'); 
            } else { 
                header.classList.remove('active'); 
                goTopBtn.classList.remove('active'); 
            } 
        });

        // Mobile Menu
        const navToggleBtn = document.querySelector('[data-nav-toggle-btn]');
        const navbar = document.querySelector('[data-navbar]');

        navToggleBtn.addEventListener('click', function() { 
            elemToggleFunc(navToggleBtn);
            elemToggleFunc(navbar);
            elemToggleFunc(document.body);
        })

        // Skills Toggling Button
        const toggleBtnBox = document.querySelector('[data-toggle-box]');
        const toggleBtns = document.querySelectorAll('[data-toggle-btn]');
        const skillsBox = document.querySelector('[data-skills-box]');

        for(let i = 0; i < toggleBtns.length; i++){
            toggleBtns[i].addEventListener('click', function(){
                elemToggleFunc(toggleBtnBox);

                for(let i = 0; i < toggleBtns.length; i++) { elemToggleFunc(toggleBtns[i]); }
                elemToggleFunc(skillsBox);
            });
        }

        // Dark & Light Theme Toggle
        const themeToggleBtn = document.querySelector('[data-theme-btn]');

        themeToggleBtn.addEventListener('click', function(){
            elemToggleFunc(themeToggleBtn);

            if(themeToggleBtn.classList.contains('active')){
                document.body.classList.remove('dark-theme');
                document.body.classList.add('light-theme');

                localStorage.setItem('theme', 'light-theme');
            }else{
                document.body.classList.add('dark-theme');
                document.body.classList.remove('light-theme');

                localStorage.setItem('theme', 'dark-theme');
            }
        })

        //Applying Theme kept in Local Storage 
        if(localStorage.getItem('theme') === 'light-theme'){
            themeToggleBtn.classList.add('active');
            document.body.classList.remove('dark-theme');
            document.body.classList.add('light-theme');
        }else{
            themeToggleBtn.classList.remove('active');
            document.body.classList.remove('light-theme');
            document.body.classList.add('dark-theme');
        }

        // Modal functionality
        const cvModal = document.getElementById('cvModal');
        const hireModal = document.getElementById('hireModal');
        const downloadCvBtn = document.getElementById('downloadCvBtn');
        const hireMeBtn = document.getElementById('hireMeBtn');
        const cancelCv = document.getElementById('cancelCv');
        const confirmCv = document.getElementById('confirmCv');
        const cancelHire = document.getElementById('cancelHire');
        const confirmHire = document.getElementById('confirmHire');
        const loadMorePhotos = document.getElementById('loadMorePhotos');
        const contactForm = document.getElementById('contactForm');

        // Show CV modal
        downloadCvBtn.addEventListener('click', function() {
            cvModal.style.display = 'flex';
        });

        // Show Hire modal
        hireMeBtn.addEventListener('click', function() {
            hireModal.style.display = 'flex';
        });

        // Close CV modal
        cancelCv.addEventListener('click', function() {
            cvModal.style.display = 'none';
        });

        // Confirm CV download
        confirmCv.addEventListener('click', function() {
            alert('Your CV download has started!');
            cvModal.style.display = 'none';
        });

        // Close Hire modal
        cancelHire.addEventListener('click', function() {
            hireModal.style.display = 'none';
        });

        // Confirm Hire
        confirmHire.addEventListener('click', function() {
            alert('Your message has been sent! I will get back to you soon.');
            hireModal.style.display = 'none';
        });

        // Load more photos functionality
        loadMorePhotos.addEventListener('click', function() {
            alert('Loading more photos...');
            // In a real implementation, this would fetch more photos from a server
        });

        // Contact form submission
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for your message! I will get back to you soon.');
            contactForm.reset();
        });

        // Close modals when clicking outside
        window.addEventListener('click', function(e) {
            if (e.target === cvModal) {
                cvModal.style.display = 'none';
            }
            if (e.target === hireModal) {
                hireModal.style.display = 'none';
            }
        });
    