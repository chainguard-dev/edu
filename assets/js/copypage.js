document.addEventListener('DOMContentLoaded', function() {
  const copyButton = document.querySelector('.copy-page-btn');
  const tooltip = document.querySelector('.copy-tooltip');
  
  if (!copyButton) return;
  
  copyButton.addEventListener('click', async function() {
    const content = await getPageAsMarkdown();
    
    if (content && await copyToClipboard(content)) {
      // Show success state
      copyButton.classList.add('copy-success');
      tooltip.classList.add('show');
      
      // Update button text
      const textElement = copyButton.querySelector('.copy-btn-text');
      const originalText = textElement ? textElement.textContent : '';
      if (textElement) {
        textElement.textContent = 'Copied to clipboard!';
      }
      
      // Reset after 2 seconds
      setTimeout(() => {
        copyButton.classList.remove('copy-success');
        tooltip.classList.remove('show');
        if (textElement) {
          textElement.textContent = originalText;
        }
      }, 2000);
    }
  });
});

async function getPageAsMarkdown() {
  const article = document.querySelector('main.docs-content');
  if (!article) return '';
  
  // Get page title
  const title = document.querySelector('h1')?.textContent || document.title;
  
  // Get page description
  const description = document.querySelector('meta[name="description"]')?.content || '';
  
  // Get main content
  let mainContent = article.cloneNode(true);
  
  // Remove elements that shouldn't be included
  const elementsToRemove = [
    '.back-button',
    '.contributors',
    '.tag-container',
    '.page-footer-meta',
    '.copy-page-btn',
    '.copy-tooltip',
    '.notice',
    '.rumble-comparison',
    '.rumble-vuln',
    '.tooltip-container',
    '.tooltip',
    '.top-container',
    '.expand-btn-container',
    'nav',
    'script',
    'style'
  ];
  
  elementsToRemove.forEach(selector => {
    mainContent.querySelectorAll(selector).forEach(el => el.remove());
  });
  
  // Build markdown
  let markdown = `# ${title}\n\n`;
  
  if (description) {
    markdown += `${description}\n\n`;
  }
  
  markdown += `Source: ${window.location.href}\n\n---\n\n`;
  markdown += convertHtmlToMarkdown(mainContent);
  
  return markdown;
}

function convertHtmlToMarkdown(element) {
  let markdown = '';
  
  const processNode = (node, listLevel = 0) => {
    if (node.nodeType === Node.TEXT_NODE) {
      // Skip whitespace-only text nodes
      const text = node.textContent;
      if (text.trim() === '') {
        return '';
      }
      return text;
    }
    
    if (node.nodeType === Node.ELEMENT_NODE) {
      const tagName = node.tagName.toLowerCase();
      let content = '';
      
      // Process children
      node.childNodes.forEach(child => {
        content += processNode(child, tagName === 'ul' || tagName === 'ol' ? listLevel + 1 : listLevel);
      });
      
      // Skip empty elements (except self-closing tags like img, hr, br)
      const selfClosingTags = ['img', 'hr', 'br'];
      if (!selfClosingTags.includes(tagName) && content.trim() === '') {
        return '';
      }
      
      // Convert based on tag
      switch (tagName) {
        case 'h1': return `# ${content.trim()}\n\n`;
        case 'h2': return `## ${content.trim()}\n\n`;
        case 'h3': return `### ${content.trim()}\n\n`;
        case 'h4': return `#### ${content.trim()}\n\n`;
        case 'h5': return `##### ${content.trim()}\n\n`;
        case 'h6': return `###### ${content.trim()}\n\n`;
        case 'p': return `${content.trim()}\n\n`;
        case 'strong':
        case 'b': return `**${content.trim()}**`;
        case 'em':
        case 'i': return `*${content.trim()}*`;
        case 'code':
          if (node.parentElement?.tagName.toLowerCase() === 'pre') {
            return content;
          }
          return `\`${content.trim()}\``;
        case 'pre':
          const codeElement = node.querySelector('code');
          if (codeElement) {
            const lang = codeElement.className.match(/language-(\w+)/)?.[1] || '';
            const codeContent = codeElement.textContent || '';
            return `\`\`\`${lang}\n${codeContent.trim()}\n\`\`\`\n\n`;
          }
          return `\`\`\`\n${content.trim()}\n\`\`\`\n\n`;
        case 'a':
          const href = node.getAttribute('href');
          if (href && !href.startsWith('#')) {
            return `[${content.trim()}](${href})`;
          }
          return content;
        case 'ul': return content + '\n';
        case 'ol': return content + '\n';
        case 'li':
          const listPrefix = node.parentElement?.tagName.toLowerCase() === 'ol' 
            ? `${Array.from(node.parentElement.children).indexOf(node) + 1}. `
            : '- ';
          const indent = '  '.repeat(listLevel - 1);
          return `${indent}${listPrefix}${content.trim()}\n`;
        case 'blockquote':
          return content.split('\n').map(line => `> ${line}`).join('\n') + '\n\n';
        case 'img':
          const alt = node.getAttribute('alt') || '';
          const src = node.getAttribute('src') || '';
          return `![${alt}](${src})\n\n`;
        case 'hr': return '---\n\n';
        case 'br': return '\n';
        case 'table': return processTable(node) + '\n\n';
        default: return content;
      }
    }
    
    return '';
  };
  
  element.childNodes.forEach(child => {
    markdown += processNode(child);
  });
  
  // Clean up excessive newlines and trim each line
  return markdown
    .split('\n')
    .map(line => line.trimEnd())
    .join('\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

function processTable(table) {
  const rows = table.querySelectorAll('tr');
  if (rows.length === 0) return '';
  
  let markdown = '';
  
  // Process header row
  const headerCells = rows[0].querySelectorAll('th, td');
  if (headerCells.length > 0) {
    markdown += '| ' + Array.from(headerCells).map(cell => cell.textContent.trim()).join(' | ') + ' |\n';
    markdown += '|' + Array.from(headerCells).map(() => ' --- ').join('|') + '|\n';
  }
  
  // Process data rows
  for (let i = headerCells.length > 0 ? 1 : 0; i < rows.length; i++) {
    const cells = rows[i].querySelectorAll('td');
    if (cells.length > 0) {
      markdown += '| ' + Array.from(cells).map(cell => cell.textContent.trim()).join(' | ') + ' |\n';
    }
  }
  
  return markdown;
}

async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    // Fallback for older browsers
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'absolute';
    textArea.style.left = '-9999px';
    document.body.appendChild(textArea);
    textArea.select();
    
    try {
      document.execCommand('copy');
      document.body.removeChild(textArea);
      return true;
    } catch (err) {
      document.body.removeChild(textArea);
      return false;
    }
  }
}