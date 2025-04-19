import { test, expect } from '@playwright/test'

test.describe('Authentication Flow', () => {
  test('should allow user to sign in', async ({ page }) => {
    // Navigate to the home page
    await page.goto('/')
    
    // Click the sign in button
    await page.click('text=Sign In')
    
    // Fill in the login form
    await page.fill('input[name="email"]', 'test@example.com')
    await page.fill('input[name="password"]', 'password123')
    
    // Submit the form
    await page.click('button[type="submit"]')
    
    // Verify successful login
    await expect(page.locator('text=Dashboard')).toBeVisible()
    await expect(page.locator('text=Welcome back')).toBeVisible()
  })

  test('should show error for invalid credentials', async ({ page }) => {
    await page.goto('/')
    await page.click('text=Sign In')
    
    await page.fill('input[name="email"]', 'wrong@example.com')
    await page.fill('input[name="password"]', 'wrongpass')
    
    await page.click('button[type="submit"]')
    
    // Verify error message
    await expect(page.locator('text=Invalid credentials')).toBeVisible()
  })
}) 