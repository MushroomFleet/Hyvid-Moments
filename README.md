# 🎬 Hyvid-Moments 🎬

## AI-Powered Context-Aware Video Prompt Sequencing

![HyVid Banner](https://img.shields.io/badge/Hunyuan-Video%20Prompting-blue)
![Version](https://img.shields.io/badge/Version-1.0.0-green)

> 🚀 **Hyvid-Moments**: Predict sequence of context-aware prompts that conform to the Hunyuan Video format!

## 📋 What is Hyvid-Moments? 

Hyvid-Moments is an innovative tool designed to generate context-aware prompt sequences for Hunyuan Video AI. Unlike traditional single-prompt generators, Hyvid-Moments specializes in reverse-engineering a narrative sequence, creating a cohesive story through multiple connected prompts that build upon each other.

By analyzing the relationships between prompts, the system creates a logical timeline of events that can be used to craft compelling video narratives with the Hunyuan Video AI model.

## 🔮 What This Project Does

Hyvid-Moments performs the following functions:

- 🧠 Predicts a sequence of context-aware prompts in reverse chronological order
- 📝 Ensures all prompts conform to the HyVid formatting guidelines
- 🔄 Creates narrative connections between sequential prompts
- 🎭 Introduces contextual story elements progressively
- 📚 Builds a complete narrative arc across multiple prompts

The system works backwards from your final scene (prompt10.txt), analyzing what must have happened earlier to lead to that moment. Each predicted prompt maintains the strict Hunyuan Video format requirements:

```
[Shot Type]: [Primary Subject Action/Description]. [Environment and Lighting Details]. [Style and Technical Specifications].
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Hyvid-Moments.git
cd Hyvid-Moments
```

2. Ensure you have VS Code with Cline installed and configured on your system, and open the "hyvid-Moments" folder.

3. No additional dependencies are required for basic functionality.

## 📈 How to Use

Using Hyvid-Moments is straightforward:

1. 📝 Add your desired final scene to `/STORY/prompt10.txt`
2. 🖥️ Run the special prompt located in `prompts/10-prompts.txt` using Cline:
   ```
   copy & paste into cline
   ```
3. 🎯 The system will analyze your prompt10.txt and generate a sequence of preceding prompts (prompt09.txt through prompt00.txt)
4. 🧩 Each new prompt will be saved to the STORY directory
5. 📊 Review the complete narrative sequence from prompt00.txt to prompt10.txt

The generated sequence will tell a complete story, with each prompt building on the previous ones while introducing new contextual elements.

## 🔄 Prompt Collection Utility

The repository includes a `prompt_collector.py` script to help manage your generated prompts:

```python
# Run the collector script
python prompt_collector.py
```

This utility:
- 📁 Collects all prompts from the `/STORY` directory
- 📎 Combines them into a single text file
- 💾 Saves the compiled file to the `/output` directory
- 🧹 Provides an option to clear the STORY directory for new projects

This is particularly useful when you want to save your generated prompt sequence or share it with others.

## 📋 Example Prompts

The system comes pre-loaded with an example in `prompt10.txt`:

```
Low-angle tracking shot: A modified Nissan 200SX drifts through a mountain descent at night, its wheels cutting through low-hanging clouds. Red warning lights catch the pearl white paint and tire smoke, while distant trains thread through mountain passes. Cinematic Japanese street racing aesthetic.
```

When you run the system with this prompt, it will generate a sequence of prompts (prompt09.txt through prompt00.txt) that tells the story of how this exciting mountain drift scene came to be.

## 🧩 Project Mapping

The project adheres to a comprehensive mapping structure defined in `project-mapping.json`, which outlines:

- Shot type specifications (required)
- Core elements (subject, environment, lighting, style)
- Technical parameters (movement, composition, lens, duration)
- Length guidelines for different types of scenes
- Quality checklist for effective prompts
- Common issues to avoid

## 🙏 Acknowledgments

A huge thank you to the brilliant minds behind **Hunyuan Video** for creating the revolutionary AI video generation system that makes this project possible! Their groundbreaking work in video synthesis technology has opened new frontiers for creative expression.

Special thanks to the Hunyuan team at Tencent for their innovative approach to AI video generation and their comprehensive prompt formatting guidelines that serve as the foundation for this project.

## 📜 License

This project is available under the MIT License - see the LICENSE file for details.

---

💫 **Created with AI assistance for the AI video generation community** 💫
