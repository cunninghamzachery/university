Reading _Understanding Cryptology_ by Christof Paar & Jan Pelzl, taking notes here. 

I will organize my notes based on sections of the book. External sources will be cited as they're used.

# Understanding Cryptology

## 1 Introduction to Cryptography and Data Security

### 1.1 Overview of Cryptology

### 1.2 Symmetric Cryptography

#### 1.2.1 Basics

#### 1.2.2 Simple Symmetric Encryption: The Substitution Cipher

### 1.3 Cryptanalysis

#### 1.3.1 General Thoughts on Breaking Cryptosystems

#### 1.3.2 How Many Key Bits Are Enough? 

### 1.4 Modular Arithmetic and More Historical Ciphers 

#### 1.4.1 Modular Arithmetic

#### 1.4.2 Integer Rings 

#### 1.4.3 Shift Cipher (or Caesar Cipher)

#### 1.4.4 Affine Cipher 

### 1.5 Discussion and Further Reading 

### 1.6 Lessons Learned

### 1.7 Problems

## 2 Stream Ciphers

### 2.1 Introduction

#### 2.1.1 Stream Ciphers vs. Block Ciphers

#### 2.1.2 Encryption and Decryption with Stream Ciphers

### 2.2 Random Numbers and an Unbreakable Stream Cipher

#### 2.2.1 Random Number Generators

#### 2.2.2 The One-Time Pad

#### 2.2.3 Towards Practical Stream Ciphers

### 2.3 Shift Register-Based Stream Ciphers

#### 2.3.1 Linear Feedback Shift Registers (LFSR)

#### 2.3.2 Known-Plaintext Attack Against Single LFSRs

#### 2.3.3 Trivium

### 2.4 Discussion and Further Reading

### 2.5 Lessons Learned

## 3 The Data Encryption Standard (DES) and Alternatives

### 3.1 Introduction to DES

#### 3.1.1 Confusion and Diffusion

### 3.2 Overview of the DES Algorithm

### 3.3 Internal Structure of DES

#### 3.3.1 Initial and Final Permutation

#### 3.3.2 The f -Function

#### 3.3.3 Key Schedule

### 3.4 Decryption

### 3.5 Security of DES

#### 3.5.1 Exhaustive Key Search

#### 3.5.2 Analytical Attacks

### 3.6 Implementation in Software and Hardware

### 3.7 DES Alternatives

#### 3.7.1 The Advanced Encryption Standard (AES) and the AES Finalist Ciphers

#### 3.7.2 Triple DES (3DES) and DESX

#### 3.7.3 Lightweight Cipher PRESENT

### 3.8 Discussion and Further Reading

### 3.9 Lessons Learned

## 4 The Advanced Encryption Standard (AES)

### 4.1 Introduction

### 4.2 Overview of the AES Algorithm

### 4.3 Some Mathematics: A Brief Introduction to Galois Fields

#### 4.3.1 Existence of Finite Fields

#### 4.3.2 Prime Fields

#### 4.3.3 Extension Fields GF(2m)

#### 4.3.4 Addition and Subtraction in GF(2m)

#### 4.3.5 Multiplication in GF(2m)

#### 4.3.6 Inversion in GF(2m)

### 4.4 Internal Structure of AES

#### 4.4.1 Byte Substitution Layer

#### 4.4.2 Diffusion Layer

#### 4.4.3 Key Addition Layer

#### 4.4.4 Key Schedule

### 4.5 Decryption

### 4.6 Implementation in Software and Hardware

### 4.7 Discussion and Further Reading

### 4.8 Lessons Learned

## 5 More About Block Ciphers

### 5.1 Encryption with Block Ciphers: Modes of Operation

#### 5.1.1 Electronic Codebook Mode (ECB)

#### 5.1.2 Cipher Block Chaining Mode (CBC)

#### 5.1.3 Output Feedback Mode (OFB)

#### 5.1.4 Cipher Feedback Mode (CFB)

#### 5.1.5 Counter Mode (CTR)

#### 5.1.6 Galois Counter Mode (GCM)

### 5.2 Exhaustive Key Search Revisited

### 5.3 Increasing the Security of Block Ciphers

#### 5.3.1 Double Encryption and Meet-in-the-Middle Attack

#### 5.3.2 Triple Encryption

#### 5.3.3 Key Whitening

### 5.4 Discussion and Further Reading

### 5.5 Lessons Learned

## 6 Introduction to Public-Key Cryptography

### 6.1 Symmetric vs. Asymmetric Cryptography

### 6.2 Practical Aspects of Public-Key Cryptography

#### 6.2.1 Security Mechanisms

#### 6.2.2 The Remaining Problem: Authenticity of Public Keys

#### 6.2.3 Important Public-Key Algorithms

#### 6.2.4 Key Lengths and Security Levels

### 6.3 Essential Number Theory for Public-Key Algorithms

#### 6.3.1 Euclidean Algorithm

#### 6.3.2 Extended Euclidean Algorithm

#### 6.3.3 Euler’s Phi Function

#### 6.3.4 Fermat’s Little Theorem and Euler’s Theorem

### 6.4 Discussion and Further Reading

### 6.5 Lessons Learned

## 7 The RSA Cryptosystem

### 7.1 Introduction

### 7.2 Encryption and Decryption

### 7.3 Key Generation and Proof of Correctness

### 7.4 Encryption and Decryption: Fast Exponentiation

### 7.5 Speed-up Techniques for RSA

#### 7.5.1 Fast Encryption with Short Public Exponents

#### 7.5.2 Fast Decryption with the Chinese Remainder Theorem

### 7.6 Finding Large Primes

#### 7.6.1 How Common Are Primes?

#### 7.6.2 Primality Tests

### 7.7 RSA in Practice: Padding

### 7.8 Attacks

### 7.9 Implementation in Software and Hardware

### 7.10 Discussion and Further Reading

### 7.11 Lessons Learned

## 8 Public-Key Cryptosystems Based on the Discrete Logarithm Problem

### 8.1 Diffie–Hellman Key Exchange

### 8.2 Some Algebra

#### 8.2.1 Groups

#### 8.2.2 Cyclic Groups

#### 8.2.3 Subgroups

### 8.3 The Discrete Logarithm Problem

#### 8.3.1 The Discrete Logarithm Problem in Prime Fields

#### 8.3.2 The Generalized Discrete Logarithm Problem

#### 8.3.3 Attacks Against the Discrete Logarithm Problem

### 8.4 Security of the Diffie–Hellman Key Exchange

### 8.5 The Elgamal Encryption Scheme

#### 8.5.1 From Diffie–Hellman Key Exhange to Elgamal Encryption

#### 8.5.2 The Elgamal Protocol

#### 8.5.3 Computational Aspects

#### 8.5.4 Security

### 8.6 Discussion and Further Reading

### 8.7 Lessons Learned

## 9 Elliptic Curve Cryptosystems

### 9.1 How to Compute with Elliptic Curves

#### 9.1.1 Definition of Elliptic Curves

#### 9.1.2 Group Operations on Elliptic Curves

### 9.2 Building a Discrete Logarithm Problem with Elliptic Curves

### 9.3 Diffie–Hellman Key Exchange with Elliptic Curves

### 9.4 Security

### 9.5 Implementation in Software and Hardware

### 9.6 Discussion and Further Reading

### 9.7 Lessons Learned

## 10 Digital Signatures

### 10.1 Introduction

#### 10.1.1 Odd Colors for Cars, or: Why Symmetric Cryptography Is Not Sufficient

#### 10.1.2 Principles of Digital Signatures

#### 10.1.3 Security Services

### 10.2 The RSA Signature Scheme

#### 10.2.1 Schoolbook RSA Digital Signature

#### 10.2.2 Computational Aspects

#### 10.2.3 Security

### 10.3 The Elgamal Digital Signature Scheme

#### 10.3.1 Schoolbook Elgamal Digital Signature

#### 10.3.2 Computational Aspects

#### 10.3.3 Security

### 10.4 The Digital Signature Algorithm (DSA)

#### 10.4.1 The DSA Algorithm

#### 10.4.2 Computational Aspects

#### 10.4.3 Security

### 10.5 The Elliptic Curve Digital Signature Algorithm (ECDSA)

#### 10.5.1 The ECDSA Algorithm

#### 10.5.2 Computational Aspects

#### 10.5.3 Security

### 10.6 Discussion and Further Reading

### 10.7 Lessons Learned

## 11 Hash Functions

### 11.1 Motivation: Signing Long Messages

### 11.2 Security Requirements of Hash Functions

#### 11.2.1 Preimage Resistance or One-Wayness

#### 11.2.2 Second Preimage Resistance or Weak Collision Resistance

#### 11.2.3 Collision Resistance and the Birthday Attack

### 11.3 Overview of Hash Algorithms

#### 11.3.1 Dedicated Hash Functions: The MD4 Family

#### 11.3.2 Hash Functions from Block Ciphers

### 11.4 The Secure Hash Algorithm SHA-1

#### 11.4.1 Preprocessing

#### 11.4.2 Hash Computation

#### 11.4.3 Implementation

### 11.5 Discussion and Further Reading

### 11.6 Lessons Learned

## 12 Message Authentication Codes (MACs)

### 12.1 Principles of Message Authentication Codes

### 12.2 MACs from Hash Functions: HMAC

### 12.3 MACs from Block Ciphers: CBC-MAC

### 12.4 Galois Counter Message Authentication Code (GMAC)

### 12.5 Discussion and Further Reading

### 12.6 Lessons Learned

## 13 Key Establishment

### 13.1 Introduction

#### 13.1.1 Some Terminology

#### 13.1.2 Key Freshness and Key Derivation

#### 13.1.3 The n2 Key Distribution Problem

### 13.2 Key Establishment Using Symmetric-Key Techniques

#### 13.2.1 Key Establishment with a Key Distribution Center

#### 13.2.2 Kerberos

#### 13.2.3 Remaining Problems with Symmetric-Key Distribution

### 13.3 Key Establishment Using Asymmetric Techniques

#### 13.3.1 Man-in-the-Middle Attack

#### 13.3.2 Certificates

#### 13.3.3 Public-Key Infrastructures (PKI) and CAs

### 13.4 Discussion and Further Reading

### 13.5 Lessons Learned
