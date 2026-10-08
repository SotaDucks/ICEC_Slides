# Designing the Disengagement Experience in Short-Form Video Use: A Diving-Metaphor Prototype

本文档包含两部分：**Slides 1–6** 总结进入 **3 Prototype Design** 之前的研究背景与相关工作；**Slides 7–10** 总结 **4 Preliminary User Study** 及之后的内容，包括研究结果、初步见解、未来工作与致谢，排除文献列表。第 3 节原型设计未纳入。正文保留英文，仅精简、合并原文内容，引用编号沿用原论文。每页的原文位置标注在 Markdown 注释中。

---

## Slide 1: SFV Use and the Exit Problem

- Short-form video (SFV) platforms have become one of the most popular forms of everyday entertainment [1].
- Globally, **87.5% of adults** report watching short videos at least once a week, spending an average of **57 minutes per day**.
- Infinite scroll, autoplay, and swipe-based navigation sustain continuous attention [2, 3]. Users may continue watching beyond their original intention because the interface offers few natural cues for disengagement [4].
- SFV use raises a design problem: how attention is captured, and how the experience of leaving might be shaped.

<!-- 原文位置：1 Introduction，PDF 第 1 页。 -->

---

## Slide 2: SFV as Hard-to-Exit Systems

- SFV platforms are engagement-optimized systems designed to maximize users' watch time [6]. Infinite scroll, autoplay, and algorithmic feeds reduce decision-making demands and support prolonged interaction.
- Infinite scroll reduces the mental and physical effort required to continue. Autoplay compresses the time available for reflection, breaks, or deliberate choice [8, 9].
- In streaming research, rapid autoplay countdowns pressured users to continue before fully processing what they had watched. In social media studies, default feeds encouraged continued scrolling unless explicit stop criteria were reintroduced [9, 10].
- Infinite-scroll interfaces are linked to mindless scrolling, reduced awareness, and a sense that users' original session goals were not fulfilled [8].

<!-- 原文位置：2.1 SFV as hard-to-exit systems，PDF 第 2 页，第 1–2 段。 -->

---

## Slide 3: Scroll Immersion and the Intention to Stop

- Alruwaili identifies **“scroll immersion”** as habitual and unintentional engagement associated with attention difficulties, working-memory disruption, and cognitive fatigue [7].
- Hard-to-exit environments may weaken the cognitive conditions required to remember and enact the intention to stop.
- Chiossi et al. found that SFV feeds significantly impaired **prospective memory** relative to Twitter, YouTube, and no-media conditions [11].
- Brief videos and rapid context switching may disrupt users' ability to recall and act upon prior intentions, including the intention to disengage [11].

<!-- 原文位置：2.1 SFV as hard-to-exit systems，PDF 第 2 页，第 1 段及第 3 段。 -->

---

## Slide 4: Design for Disengagement

- Recent work frames disengagement as a necessary phase within the dynamics of engagement [12, 13].
- Alexandrovsky et al. argue that disengagement from games can be designed to support **self-determined exit** [5].
- Positive disengagement is associated with **satisfaction and closure**. **Agency and a sense of control** are central to how players experience leaving play [5].
- Leaving is an experiential phase whose quality can be intentionally shaped and evaluated.

<!-- 原文位置：2.2 Design for disengagement，PDF 第 2–3 页，第 1 段。 -->

---

## Slide 5: Disengagement in Media Use

- Media-use theories have historically explained selection and engagement better than disengagement, although media use unfolds as a temporal process with both a beginning and an end [14].
- Stopping can arise from external interruption or from changing qualities of the experience itself over the course of use [14].
- Ernst and Schnauber identified **internal, environmental, and media-context cues** that prompt users to stop on TikTok and Instagram [15].
- Disengagement may take multiple forms rather than converge on a single endpoint [15].

<!-- 原文位置：2.2 Design for disengagement，PDF 第 3 页，第 2 段。 -->

---

## Slide 6: Research Gap and Aim

- It remains unclear how SFV interfaces might actively support a more constructive exit experience.
- This paper explores whether **metaphorical gameful design**, structured around a diving metaphor, can make SFV disengagement more **noticeable and agentic**.
- The design aims to embed stopping within an internally coherent experiential frame, with attention to **closure, perceived choice, valence, and related affective appraisal**.
- The contribution is a preliminary investigation of disengagement support in SFV use. It provides an initial test of more gameful, perceptual, and noticeable disengagement while fostering closure and autonomy, without claiming long-term prevention of overuse.

<!-- 原文位置：Abstract，PDF 第 1 页；1 Introduction 最后一段，PDF 第 2 页；2.2 Design for disengagement 最后一段，PDF 第 3 页。 -->

---

## Slide 7: Preliminary User Study

**Research question:** Does Scroll Dive support a positive exit experience in SFV use, in terms of closure, perceived control/agency, and post-exit appraisal?

- **Design and participants:** A between-subjects study with **25 participants**: **13** in the Scroll Dive condition and **12** in the frictional control condition.
- **Control condition:** The core diving metaphor was removed, and game-like interface expressions were replaced with neutral, non-metaphorical ones. Disengagement support relied primarily on frictional cues.
- **Content and duration:** Both conditions used a pool of **50 animal-themed short videos** selected from highly popular TikTok content. Animal videos were chosen as less dependent on topical preferences than politics, beauty, or gaming. Recommended Maximum Watch Time was **180 seconds** in both conditions.
- **Procedure:** Participants received a standardized introduction, provided consent, and browsed naturally. They could stop voluntarily before the limit. Otherwise, the session ended at the maximum duration.
- **Measurement:** Immediately after the session, closure was assessed with a single Likert-type item [5], perceived control with the **IMI Perceived Choice** subscale [16], and affective appraisal with **SAM Valence and Arousal** [17]. All Likert-style items used **5-point scales**.

<!-- 原文位置：4 Preliminary User Study、4.1 Research Questions、4.2 Study design、4.3 Measurement，PDF 第 5 页。 -->

---

## Slide 8: Study Results

Perceived choice and arousal met the requirements for parametric analysis and were compared using independent-samples **t-tests**. Closure and valence did not meet the normality assumption and were analyzed using **Mann–Whitney U tests**.

| Measure | Scroll Dive | Frictional control | Statistic | p-value |
| --- | --- | --- | --- | --- |
| Perceived choice | Mean = 3.37 (0.29) | Mean = 3.16 (0.15) | t = 2.08 | .050 |
| Arousal | Mean = 3.83 (0.58) | Mean = 2.55 (0.52) | t = 5.59 | .001 |
| Closure | Mean rank = 13.04 | Mean rank = 10.86 | U = 53.50, Z = -0.85 | .394 |
| Valence | Mean rank = 13.63 | Mean rank = 10.23 | U = 46.50, Z = -1.56 | .119 |

- Scroll Dive **significantly increased arousal** and produced a **borderline significant increase in perceived choice**, suggesting a more activating and somewhat more autonomy-supportive disengagement experience.
- **No significant differences** were found for closure or valence, which may partly reflect the limited sample size. Both were directionally higher in Scroll Dive, but the data do not support a reliable improvement in the sense of completion or the pleasantness of exit.

<!-- 原文位置：4.4 Results、Table 1、Table 2，PDF 第 6–7 页。括号内数值按 Table 1 保留，原文未明确标注其含义；未自行将其解释为标准差或标准误。 -->

---

## Slide 9: Preliminary Insights

Overall, the findings suggest that Scroll Dive made disengagement feel more **noticeable and agentic** than the frictional control condition.

- **A gameful metaphor may make stopping a natural progression.** Oxygen depletion provides an internally coherent rationale within a make-believe frame. Stopping may feel less like imposed persuasion and more like a natural next step within the experience.
- **Disengagement design may make stopping more noticeable rather than more pleasant.** The strongest effect appeared in arousal, rather than valence or closure. In SFV contexts, disengagement support may initially work by making the ending more perceptually and experientially prominent, without directly making it feel more positive or resolved.
- **A structured ending alone may not support closure.** The absence of a significant difference in closure suggests that a meaningful, metaphorically organized exit does not automatically create a stronger sense of completion. SFV viewing is often continuous, open-ended, and lacks a clear endpoint, making closure challenging to design for.

<!-- 原文位置：5.1 Preliminary insights，PDF 第 7 页。以上保留原文的初步解释及不确定性，不将其表述为已证实的机制。 -->

---

## Slide 10: Limitations and Future Work

- **Preliminary scope:** The study is limited in its design, sample size, and control conditions.
- **Everyday and longer-term use:** Examine repeated use in contexts closer to everyday SFV browsing to determine whether the observed effects remain stable beyond a single-session evaluation.
- **Alternative metaphors and framing:** Compare the diving metaphor with other disengagement metaphors or framing strategies to clarify whether the effects are specific to this design or reflect a broader principle of metaphorical disengagement support.
- **Qualitative investigation:** Explore how users perceive the disengagement process and make sense of the metaphor.
- **Broader assessment:** Consider additional measures, including satisfaction with stopping, perceived interruption, and post-exit reflection.

**Acknowledgements:** Supported by the Youth Project of the Guangdong Provincial Philosophy and Social Science Planning Project (**Grant No. GD25YYS15**), “Ethical Research on Dark Patterns in User Experience Design: A Case Study of Short-Form Video Addiction.”

<!-- 原文位置：4 Preliminary User Study 开头，PDF 第 5 页；5.2 Future work，PDF 第 7 页；Acknowledgements，PDF 第 8 页。 -->
