/* ==========================================================================
   PNK Mobile Store - Custom JS Helpers (AOS, Theme, SweetAlert, HTMX)
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function () {
    // 1. Initialize AOS (Animate On Scroll) if present
    if (typeof AOS !== "undefined") {
        AOS.init({
            duration: 800,
            easing: "ease-in-out",
            once: true,
            mirror: false
        });
    }

    // 2. Theme Switcher Initial Load
    const savedTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);

    // 3. Auto initialize Django messages across all pages
    initDjangoMessages();
});

// 4. Smart System Messages Formatter & Khmer Localization
function formatSystemMessage(text, tag = "") {
    const raw = (text || "").trim();
    if (!raw) return { title: "", text: "", type: tag || "info" };

    const tagStr = String(tag || "").toLowerCase();

    // 1. Allauth: Successfully signed in as <email/username>
    const signInMatch = raw.match(/Successfully signed in as\s+([^.]+)\.?/i);
    if (signInMatch) {
        const userEmail = signInMatch[1].trim();
        return {
            title: "ចូលគណនីជោគជ័យ",
            text: `សូមស្វាគមន៍មកកាន់ PNK SHOP (<span class="text-success fw-bold">${userEmail}</span>)`,
            type: "success"
        };
    }

    // 2. Allauth: Successfully signed out
    if (/Successfully signed out\.?/i.test(raw)) {
        return {
            title: "ចាកចេញជោគជ័យ",
            text: "អ្នកបានចាកចេញពីគណនីដោយសុវត្ថិភាព",
            type: "info"
        };
    }

    // 3. Allauth / Django: You have signed up successfully
    if (/You have signed up successfully\.?/i.test(raw)) {
        return {
            title: "ចុះឈ្មោះជោគជ័យ",
            text: "គណនីរបស់អ្នកត្រូវបានបង្កើតរួចរាល់ សូមស្វាគមន៍!",
            type: "success"
        };
    }

    // 4. Password changes
    if (/Password (successfully set|changed successfully)\.?/i.test(raw)) {
        return {
            title: "ប្តូរពាក្យសម្ងាត់ជោគជ័យ",
            text: "ពាក្យសម្ងាត់ថ្មីរបស់អ្នកត្រូវបានកំណត់រួចរាល់",
            type: "success"
        };
    }

    // 5. Email confirmation
    if (/Confirmation e-mail sent/i.test(raw)) {
        return {
            title: "បានផ្ញើអ៊ីមែលផ្ទៀងផ្ទាត់",
            text: "យើងបានផ្ញើតំណភ្ជាប់ផ្ទៀងផ្ទាត់ទៅកាន់អ៊ីមែលរបស់អ្នក",
            type: "info"
        };
    }

    return {
        title: "",
        text: raw,
        type: tagStr || (raw.includes("ជោគជ័យ") ? "success" : raw.includes("បញ្ហា") || raw.includes("បរាជ័យ") ? "error" : "info")
    };
}

// 5. Centralized Notification Toast Helper (Unified luxury design across all pages)
function showToast(message, isError = false, title = "") {
    const formatted = formatSystemMessage(message, isError);
    let finalMessage = formatted.text;
    let finalTitle = title || formatted.title;
    let finalType = formatted.type;

    let iconType = "success";
    let statusClass = "toast-success";
    
    // Normalize message type from tag string or boolean
    const tagStr = String(finalType || "").toLowerCase();
    if (finalType === true || tagStr.includes("error") || tagStr.includes("danger")) {
        iconType = "error";
        statusClass = "toast-error";
    } else if (tagStr.includes("warning")) {
        iconType = "warning";
        statusClass = "toast-warning";
    } else if (tagStr.includes("info")) {
        iconType = "info";
        statusClass = "toast-info";
    } else {
        iconType = "success";
        statusClass = "toast-success";
    }

    if (!finalTitle) {
        if (iconType === "success") finalTitle = "ជោគជ័យ";
        else if (iconType === "error") finalTitle = "មានបញ្ហា";
        else if (iconType === "warning") finalTitle = "ប្រុងប្រយ័ត្ន";
        else finalTitle = "ជូនដំណឹង";
    }

    const toastHtml = `
        <div class="pnk-toast-wrapper">
            <div class="pnk-toast-header-title">${finalTitle}</div>
            <div class="pnk-toast-message-body">${finalMessage}</div>
        </div>
    `;

    if (typeof Swal !== "undefined") {
        Swal.fire({
            toast: true,
            position: "top-end",
            icon: iconType,
            html: toastHtml,
            showConfirmButton: false,
            showCloseButton: true,
            timer: 4000,
            timerProgressBar: true,
            customClass: {
                popup: `swal2-toast pnk-luxury-toast ${statusClass}`,
                htmlContainer: "pnk-toast-container-override",
                closeButton: "pnk-toast-close-btn",
                timerProgressBar: "pnk-toast-progress"
            }
        });
    } else {
        alert(finalMessage);
    }
}

// 6. Automatic Django messages loader
function initDjangoMessages() {
    const msgContainers = document.querySelectorAll(
        "#django-messages-list li:not([data-toast-processed]), #django-messages-list span:not([data-toast-processed]), #django-messages .django-message:not([data-toast-processed]), #django-messages-data .django-message-item:not([data-toast-processed])"
    );
    msgContainers.forEach(item => {
        item.setAttribute("data-toast-processed", "true");
        const tag = item.getAttribute("data-tags") || item.getAttribute("data-tag") || "";
        const text = item.getAttribute("data-text") || item.innerText || "";
        if (text.trim()) {
            showToast(text.trim(), tag);
        }
    });
}


